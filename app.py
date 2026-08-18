import streamlit as st
import time
import sys
import os
import random
from pipeline import run_research_pipeline
from ui.components import render_sidebar
from ui.styles import inject_custom_css

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Page configuration
st.set_page_config(
    page_title="ScholarAI - Research Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS
inject_custom_css()

# Initialize session state
def init_session_state():
    defaults = {
        "messages": [],
        "current_prompt": "",
        "is_generating": False,
        "research_state": None,
        "chat_history": [],
        "user_name": "Researcher",
        "max_chars": 1000,
        "prompt_suggestions": [
            {
                "title": "AI Research",
                "prompt": "Explain the latest developments in transformer-based AI architectures"
            },
            {
                "title": "RAG Systems",
                "prompt": "How do Retrieval Augmented Generation (RAG) systems work and what are their applications?"
            },
            {
                "title": "Agentic AI",
                "prompt": "What are AI agents and how are they being used in enterprise applications?"
            },
            {
                "title": "Language Models",
                "prompt": "Compare different language models and their use cases in research"
            }
        ]
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

# Handle prompt submission
def handle_prompt_submission(prompt):
    if not prompt or st.session_state.is_generating:
        return
    
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    st.session_state.is_generating = True
    st.session_state.current_prompt = prompt
    
    try:
        # Create a placeholder for progress
        progress_placeholder = st.empty()
        
        # Show progress stages
        stages = ["🔍 Searching", "📄 Reading", "✍️ Drafting", "🔬 Reviewing"]
        for i, stage in enumerate(stages):
            progress_html = f"""
            <div style="padding: 12px 20px; background: #111111; border: 1px solid #292929; border-radius: 8px; margin: 16px auto; max-width: 900px; text-align: center; color: #A1A1A1;">
                <span style="font-size: 14px;">{'●' * (i+1)}{'○' * (3-i)} {stage}...</span>
            </div>
            """
            progress_placeholder.markdown(progress_html, unsafe_allow_html=True)
            time.sleep(0.3)
        
        # Clear progress
        progress_placeholder.empty()
        
        # Execute pipeline
        print(f"\n{'='*50}")
        print(f"Running pipeline for: {prompt}")
        print(f"{'='*50}\n")
        
        result = run_research_pipeline(prompt)
        
        # Debug: Print what we got from the pipeline
        print(f"\n{'='*50}")
        print("PIPELINE RESULT KEYS:", result.keys())
        print(f"{'='*50}")
        
        # Get the report - handle different possible return formats
        report_content = result.get('report', '')
        if not report_content:
            # Try alternative keys
            report_content = result.get('output', '')
        if not report_content:
            # If still empty, use the entire result as fallback
            report_content = str(result)
        
        # Ensure we have content to display
        if not report_content or report_content == '{}':
            report_content = "No report was generated. Please check the pipeline output in the terminal."
        
        # Add assistant response
        st.session_state.messages.append({
            "role": "assistant",
            "content": report_content,
            "sources": result.get('search_results', 'No sources available.'),
            "feedback": result.get('feedback', 'No feedback available.'),
            "scraped": result.get('scraped_content', 'No scraped content available.')
        })
        
        # Add to chat history
        st.session_state.chat_history.append({
            "query": prompt,
            "timestamp": time.time()
        })
        
        # Force a rerun to display the new message
        st.rerun()
        
    except Exception as e:
        import traceback
        error_msg = traceback.format_exc()
        print(f"ERROR: {error_msg}")
        
        # Add error message to chat
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"❌ **Error occurred:**\n\n{str(e)}\n\nPlease check the terminal for details."
        })
        st.rerun()
    
    finally:
        st.session_state.is_generating = False

# Refresh prompts function
def refresh_prompts():
    random.shuffle(st.session_state.prompt_suggestions)
    st.rerun()

# Render chat input function
def render_chat_input():
    """Render the chat input component"""
    st.markdown("""
    <div class="chat-input-container">
        <div class="chat-input-wrapper">
    """, unsafe_allow_html=True)
    
    # Text input
    col1, col2 = st.columns([5, 1])
    with col1:
        prompt = st.text_area(
            "Ask whatever you want...",
            key="input_prompt",
            height=80,
            placeholder="Enter a research topic...",
            label_visibility="collapsed",
            disabled=st.session_state.is_generating
        )
    
    with col2:
        # Character counter
        char_count = len(prompt) if prompt else 0
        st.markdown(f"""
        <div style="text-align: right; color: #707070; font-size: 12px; margin-top: 60px;">
            {char_count}/{st.session_state.max_chars}
        </div>
        """, unsafe_allow_html=True)
        
        # Send button
        send_disabled = not prompt or st.session_state.is_generating
        if st.button("➜", key="send_button", disabled=send_disabled, use_container_width=True):
            handle_prompt_submission(prompt)
            st.session_state.input_prompt = ""
            st.rerun()
    
    # Attachments section
    st.markdown("""
    <div class="chat-input-footer">
        <div class="attachment-options">
            <span class="attachment-option">📎 Add Attachment</span>
            <span class="attachment-option">🖼 Use Image</span>
        </div>
        <div class="tool-selector">
            <span class="tool-option">All Web ▾</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

# Render welcome with better button handling
def render_welcome_with_buttons(user_name, prompt_suggestions, on_prompt_select):
    """Render the welcome section with prompt suggestion buttons"""
    st.markdown(f"""
    <div class="welcome-section">
        <h1 class="welcome-title">Hi there, {user_name}</h1>
        <h2 class="welcome-subtitle">What would you like to research?</h2>
        <p class="welcome-description">Use one of the suggested topics below or enter your own to begin research</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Render prompt cards as buttons
    cols = st.columns(4)
    for idx, suggestion in enumerate(prompt_suggestions[:4]):
        with cols[idx]:
            # Use a button with custom styling
            if st.button(
                suggestion['prompt'],
                key=f"prompt_btn_{idx}",
                use_container_width=True,
                type="secondary"
            ):
                on_prompt_select(suggestion['prompt'])

# --- MAIN APP ---

# Render sidebar
render_sidebar()

# Main content
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Check if we have a conversation
    if not st.session_state.messages:
        render_welcome_with_buttons(
            user_name=st.session_state.user_name,
            prompt_suggestions=st.session_state.prompt_suggestions,
            on_prompt_select=handle_prompt_submission
        )
        
        # Refresh prompts button
        col_refresh1, col_refresh2, col_refresh3 = st.columns([1, 1, 1])
        with col_refresh2:
            if st.button("↻ Refresh Prompts", key="refresh_btn", use_container_width=True):
                refresh_prompts()
    else:
        # Display all messages
        for message in st.session_state.messages:
            if message['role'] == 'user':
                st.markdown(f"""
                <div class="chat-message user">
                    <div class="message-avatar">👤</div>
                    <div class="message-content">
                        <div class="message-role">You</div>
                        <div class="message-text">{message['content']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                # Assistant message
                st.markdown(f"""
                <div class="chat-message assistant">
                    <div class="message-avatar">🤖</div>
                    <div class="message-content">
                        <div class="message-role">Assistant</div>
                        <div class="message-text">{message['content']}</div>
                """, unsafe_allow_html=True)
                
                # Show expandable sections for additional data
                if 'sources' in message and message['sources'] and message['sources'] != 'No sources available.':
                    with st.expander("📚 Sources & Research Data"):
                        st.markdown("**Search Results:**")
                        st.text(message['sources'][:1000] + "..." if len(message['sources']) > 1000 else message['sources'])
                        
                        if 'scraped' in message and message['scraped'] and message['scraped'] != 'No scraped content available.':
                            st.markdown("**Scraped Content:**")
                            st.text(message['scraped'][:1000] + "..." if len(message['scraped']) > 1000 else message['scraped'])
                
                if 'feedback' in message and message['feedback'] and message['feedback'] != 'No feedback available.':
                    with st.expander("🔬 Critic's Feedback"):
                        st.markdown(message['feedback'])
                
                st.markdown("</div></div>", unsafe_allow_html=True)
        
        # Show generating indicator if in progress
        if st.session_state.is_generating:
            st.markdown("""
            <div class="chat-message assistant">
                <div class="message-avatar">🤖</div>
                <div class="message-content">
                    <div class="message-role">Assistant</div>
                    <div class="message-text thinking">
                        <span class="thinking-dot">●</span> Researching...
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Chat input (only show if not generating)
    if not st.session_state.is_generating:
        render_chat_input()
    else:
        st.info("⏳ Research in progress... Please wait.")