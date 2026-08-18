import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from tools import scrape_url, web_search

load_dotenv()

try:
    from langchain_mistralai import ChatMistralAI
except Exception:  # pragma: no cover - optional vendor package
    ChatMistralAI = None

try:
    from langchain_openai import ChatOpenAI
except Exception:  # pragma: no cover - optional vendor package
    ChatOpenAI = None


def _get_llm():
    if os.getenv("OPENAI_API_KEY") and ChatOpenAI is not None:
        return ChatOpenAI(model="gpt-4o-mini", temperature=0)
    if os.getenv("MISTRAL_API_KEY") and ChatMistralAI is not None:
        return ChatMistralAI(model="mistral-small-2603", temperature=0)
    return None


llm = _get_llm()


class _FallbackChain:
    def __init__(self, label: str):
        self.label = label

    def invoke(self, values):
        if self.label == "writer":
            topic = values.get("topic", "")
            research = values.get("research", "")
            return (
                "LLM is not configured for this deployment. "
                "Add OPENAI_API_KEY or MISTRAL_API_KEY in the app environment.\n\n"
                f"Topic: {topic}\n\nResearch summary:\n{research[:1200]}"
            )

        report = values.get("report", "")
        return (
            "LLM is not configured for this deployment. "
            "Add OPENAI_API_KEY or MISTRAL_API_KEY to enable the critic review.\n\n"
            f"Report preview:\n{report[:1200]}"
        )


# 1ST AGENT

def build_search_agent():
    if llm is None:
        raise RuntimeError("No LLM is configured. Set OPENAI_API_KEY or MISTRAL_API_KEY before running the research pipeline.")
    return create_agent(model=llm, tools=[web_search])


# 2ND AGENT

def build_reader_agent():
    if llm is None:
        raise RuntimeError("No LLM is configured. Set OPENAI_API_KEY or MISTRAL_API_KEY before running the research pipeline.")
    return create_agent(model=llm, tools=[scrape_url])


## Writer chain

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

# chain for writer
writer_chain = writer_prompt | llm | StrOutputParser() if llm is not None else _FallbackChain("writer")

# critic ai chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser() if llm is not None else _FallbackChain("critic")