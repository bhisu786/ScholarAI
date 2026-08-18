import streamlit as st

def inject_custom_css():
    """Inject custom CSS for the application"""
    st.markdown("""
    <style>
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
        .viewerBadge_container__1QSob {display: none;}
        
        /* Global styles */
        .stApp {
            background-color: #0D0D0D;
            color: #F5F5F5;
        }
        
        .main > div {
            background-color: #0D0D0D;
        }
        
        /* Custom Sidebar */
        .custom-sidebar {
            position: fixed;
            left: 0;
            top: 0;
            height: 100vh;
            width: 64px;
            background: #151515;
            border-right: 1px solid #292929;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 20px 0;
            z-index: 1000;
        }
        
        .sidebar-top {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }
        
        .sidebar-bottom {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }
        
        .sidebar-logo {
            color: #A1A1A1;
            margin-bottom: 20px;
            padding: 4px;
        }
        
        .sidebar-icon {
            width: 36px;
            height: 36px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 6px;
            color: #707070;
            cursor: pointer;
            transition: all 0.2s ease;
            position: relative;
        }
        
        .sidebar-icon:hover {
            background: #262626;
            color: #A1A1A1;
        }
        
        .sidebar-icon.active {
            background: #262626;
            color: #F5F5F5;
        }
        
        .sidebar-avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: #2A2A2A;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #A1A1A1;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        
        .sidebar-avatar:hover {
            background: #3A3A3A;
        }
        
        /* Welcome Section */
        .welcome-section {
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px 20px 20px;
            text-align: center;
        }
        
        .welcome-title {
            font-size: 32px;
            font-weight: 700;
            color: #F5F5F5;
            margin: 0 0 4px 0;
            line-height: 1.15;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        
        .welcome-subtitle {
            font-size: 24px;
            font-weight: 400;
            color: #F5F5F5;
            margin: 0 0 12px 0;
            line-height: 1.3;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        
        .welcome-description {
            color: #8B8B8B;
            font-size: 14px;
            margin: 0 0 32px 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        
        /* Prompt Cards */
        .prompt-card {
            background: #111111;
            border: 1px solid #292929;
            border-radius: 8px;
            padding: 14px;
            min-height: 80px;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: flex-start;
            margin: 4px;
        }
        
        .prompt-card:hover {
            background: #181818;
            border-color: #404040;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        
        .prompt-card-content {
            display: flex;
            gap: 10px;
            align-items: flex-start;
        }
        
        .prompt-card-icon {
            color: #707070;
            font-size: 16px;
            flex-shrink: 0;
            margin-top: 2px;
        }
        
        .prompt-card-text {
            color: #A1A1A1;
            font-size: 13px;
            line-height: 1.4;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        
        /* Chat Input */
        .chat-input-container {
            max-width: 900px;
            margin: 0 auto;
            padding: 0 20px 20px 20px;
            position: relative;
        }
        
        .chat-input-wrapper {
            background: #191919;
            border: 1px solid #2B2B2B;
            border-radius: 14px;
            padding: 16px;
            transition: border-color 0.2s ease;
        }
        
        .chat-input-wrapper:focus-within {
            border-color: #3A3A3A;
        }
        
        .chat-input-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 12px;
            padding-top: 8px;
            border-top: 1px solid #1F1F1F;
        }
        
        .attachment-options {
            display: flex;
            gap: 16px;
        }
        
        .attachment-option {
            color: #707070;
            font-size: 13px;
            cursor: pointer;
            transition: color 0.2s ease;
        }
        
        .attachment-option:hover {
            color: #A1A1A1;
        }
        
        .tool-selector {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .tool-option {
            color: #A1A1A1;
            font-size: 13px;
            padding: 4px 12px;
            border: 1px solid #2B2B2B;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        
        .tool-option:hover {
            border-color: #404040;
            background: #1F1F1F;
        }
        
        /* Chat Messages */
        .chat-message {
            display: flex;
            gap: 12px;
            padding: 16px 20px;
            max-width: 900px;
            margin: 0 auto;
            border-bottom: 1px solid #151515;
        }
        
        .message-avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
        }
        
        .user .message-avatar {
            background: #1F1F1F;
        }
        
        .assistant .message-avatar {
            background: #1F1F1F;
        }
        
        .message-content {
            flex: 1;
            min-width: 0;
        }
        
        .message-role {
            font-size: 13px;
            font-weight: 600;
            color: #A1A1A1;
            margin-bottom: 4px;
        }
        
        .message-text {
            color: #F5F5F5;
            font-size: 15px;
            line-height: 1.6;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        
        .message-text.thinking {
            color: #A1A1A1;
        }
        
        .thinking-dot {
            animation: pulse 1.5s ease-in-out infinite;
            display: inline-block;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1; }
        }
        
        /* Research Progress */
        .research-progress-horizontal {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 16px 20px;
            background: #111111;
            border: 1px solid #292929;
            border-radius: 8px;
            margin: 16px auto;
            max-width: 900px;
            flex-wrap: wrap;
        }
        
        .progress-step {
            font-size: 13px;
            padding: 4px 8px;
            border-radius: 4px;
            white-space: nowrap;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        
        .progress-step.completed {
            color: #4CAF50;
        }
        
        .progress-step.in-progress {
            color: #F5F5F5;
            animation: pulse 1.5s ease-in-out infinite;
        }
        
        .progress-step.pending {
            color: #707070;
        }
        
        .progress-arrow {
            color: #404040;
            font-size: 12px;
            margin: 0 4px;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .custom-sidebar {
                width: 48px;
                padding: 12px 0;
            }
            
            .welcome-title {
                font-size: 24px;
            }
            
            .welcome-subtitle {
                font-size: 18px;
            }
            
            .prompt-card {
                min-height: 60px;
                padding: 10px;
            }
            
            .prompt-card-text {
                font-size: 12px;
            }
            
            .chat-input-container {
                padding: 0 12px 12px 12px;
            }
            
            .main > div {
                margin-left: 48px !important;
            }
        }
        
        @media (max-width: 480px) {
            .custom-sidebar {
                width: 40px;
                padding: 8px 0;
            }
            
            .sidebar-icon {
                width: 28px;
                height: 28px;
            }
            
            .sidebar-avatar {
                width: 24px;
                height: 24px;
                font-size: 11px;
            }
            
            .welcome-section {
                padding: 20px 12px 12px 12px;
            }
            
            .welcome-title {
                font-size: 20px;
            }
            
            .welcome-subtitle {
                font-size: 16px;
            }
            
            .main > div {
                margin-left: 40px !important;
            }
        }
        
        /* Additional Streamlit overrides */
        .stTextArea > div > div > textarea {
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            color: #F5F5F5 !important;
            font-size: 15px !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
            resize: none !important;
        }
        
        .stTextArea > div > div > textarea:focus {
            border: none !important;
            box-shadow: none !important;
        }
        
        .stTextArea > div > div {
            background-color: transparent !important;
            border: none !important;
        }
        
        /* Hide default Streamlit button styles */
        .stButton > button {
            background: transparent !important;
            border: none !important;
            color: #707070 !important;
            font-size: 20px !important;
            padding: 8px 12px !important;
            border-radius: 8px !important;
            transition: all 0.2s ease !important;
        }
        
        .stButton > button:hover:not(:disabled) {
            background: #1F1F1F !important;
            color: #F5F5F5 !important;
        }
        
        .stButton > button:disabled {
            opacity: 0.3 !important;
            cursor: not-allowed !important;
        }
        
        /* Expander customization */
        .streamlit-expanderHeader {
            background-color: #111111 !important;
            border: 1px solid #292929 !important;
            border-radius: 8px !important;
            color: #A1A1A1 !important;
            font-size: 14px !important;
        }
        
        .streamlit-expanderContent {
            background-color: #0D0D0D !important;
            border: 1px solid #292929 !important;
            border-top: none !important;
            border-radius: 0 0 8px 8px !important;
            padding: 16px !important;
        }
        
        /* Column spacing */
        .row-widget.stColumns {
            gap: 8px !important;
        }
        
        /* Ensure main content doesn't overlap sidebar */
        .main > div {
            margin-left: 64px !important;
        }
    </style>
    """, unsafe_allow_html=True)