# ui/styles.py - Add this to the existing inject_custom_css function

def inject_custom_css():
    """Inject custom CSS for the application"""
    st.markdown("""
    <style>
        /* ... existing CSS ... */
        
        /* Horizontal Research Progress */
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
        
        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }
        
        /* ... rest of existing CSS ... */
    </style>
    """, unsafe_allow_html=True)