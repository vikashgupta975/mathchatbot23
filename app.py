import streamlit as st
import os
from utils import get_mistral_response
from styles import teaching_styles, apply_style

# Page configuration
st.set_page_config(
    page_title="Math Problem Solver",
    page_icon="🧮",
    layout="wide"
)

# Initialize session state variables if they don't exist
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'selected_style' not in st.session_state:
    st.session_state.selected_style = "standard"

# Header and creator info
st.title("🧮 Math Problem Solver")
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <p>Created by:<br>
    <b>Vikash Gupta</b> (Reg: 12321380)<br>
    <b>Khushdeep Saini</b> (Reg: 12316852)<br>
    <b>Satyam Upadhyay</b> (Reg: 12318963)
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar for teaching style selection
with st.sidebar:
    st.title("Teaching Styles")
    st.write("Choose a teaching style that works best for you:")
    
    # Radio buttons for selecting teaching style
    style_options = list(teaching_styles.keys())
    selected_style = st.radio("Select Teaching Style", style_options, index=style_options.index(st.session_state.selected_style))
    
    # Update session state if style changes
    if selected_style != st.session_state.selected_style:
        st.session_state.selected_style = selected_style
        # Clear the chat when style changes
        st.session_state.messages = []
        st.rerun()
    
    # Display style description
    st.write("### About this style:")
    st.write(teaching_styles[selected_style]["description"])
    
    # Add creator information in the sidebar footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### About")
    st.sidebar.info("""
    This Math Problem Solver uses Mistral AI to provide step-by-step solutions to mathematical problems.
    
    Developed by:
    - Vikash Gupta (12321380)
    - Khushdeep Saini (12316852)
    - Satyam Upadhyay (12318963)
    """)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your math problem here...")

# Handle user input
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Solving the problem..."):
            try:
                # Get the selected style attributes
                style_attributes = teaching_styles[st.session_state.selected_style]
                
                # Apply the teaching style to the prompt
                styled_prompt = apply_style(user_input, style_attributes)
                
                # Get response from Mistral AI
                response = get_mistral_response(styled_prompt)
                
                # Display the response
                st.markdown(response)
                
                # Add assistant message to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                error_message = f"Sorry, I encountered an error: {str(e)}"
                st.error(error_message)
                st.session_state.messages.append({"role": "assistant", "content": error_message})

# Instructions for users
if not st.session_state.messages:
    st.info("""
    ### How to use this Math Problem Solver:
    
    1. Select a teaching style from the sidebar that matches your learning preference
    2. Type your math problem in the chat input below
    3. The AI will provide a step-by-step solution based on your selected teaching style
    
    **Example problems you can ask:**
    - Solve the equation: 2x + 5 = 15
    - Find the derivative of f(x) = x² + 3x - 7
    - Calculate the area of a circle with radius 5
    - Simplify the expression: (3x² - 2x + 5) + (4x² + 3x - 8)
    """)

# Reset chat button
if st.button("Reset Chat"):
    st.session_state.messages = []
    st.rerun()
