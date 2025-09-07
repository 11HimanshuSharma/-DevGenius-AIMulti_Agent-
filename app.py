"""
DevGenius AI Multi-Agent System - Main Application

This is the main Streamlit application that provides the user interface
for the AI multi-agent development team.
"""

import streamlit as st
from workflow import WorkflowManager


def setup_page_config():
    """Configure the Streamlit page settings."""
    st.set_page_config(
        page_title="DevGenius AI Multi-Agent System", 
        layout="wide",
        initial_sidebar_state="collapsed"
    )


def render_header():
    """Render the application header and description."""
    st.title("🤖 DevGenius: AI Multi-Agent Development Team")
    
    st.markdown("""
    Welcome to DevGenius! This application simulates a team of AI agents that collaborate to write, review, test, and refine code based on your request.
    Enter a feature you'd like to build below.
    """)


def render_input_form():
    """Render the user input form and return the user request."""
    user_request = st.text_input(
        "Enter your feature request:", 
        placeholder="e.g., Create a Python function to fetch and parse weather data from an API"
    )
    return user_request


def render_settings_sidebar():
    """Render the settings sidebar and return configuration options."""
    with st.sidebar:
        st.header("⚙️ Settings")
        
        max_iterations = st.slider(
            "Max Iterations",
            min_value=1,
            max_value=5,
            value=3,
            help="Maximum number of code refinement iterations"
        )
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown("""
        This application uses a multi-agent system where different AI agents collaborate:
        
        - 🤵 **Project Manager**: Analyzes and breaks down requests
        - 👨‍💻 **Developer**: Writes initial code
        - 🧐 **Code Reviewer**: Reviews for bugs and best practices  
        - 🧪 **Tester**: Creates and runs unit tests
        - 🛠️ **Refactor Agent**: Improves code based on feedback
        """)
        
    return max_iterations


def run_development_process(user_request: str, max_iterations: int):
    """Run the development process and display results."""
    with st.status("🚀 Launching the AI development team...", expanded=True) as status:
        # Initialize workflow manager
        workflow_manager = WorkflowManager(max_iterations=max_iterations)
        
        # Execute the workflow
        results = workflow_manager.execute_workflow(user_request)
        
        # Update status based on results
        if results["success"]:
            status.update(
                label="✅ Process Complete!", 
                state="complete", 
                expanded=False
            )
        else:
            status.update(
                label="❌ Process Failed!", 
                state="error", 
                expanded=False
            )

    return results


def render_results(results: dict):
    """Render the final results of the development process."""
    if results["success"]:
        st.balloons()
        st.write("---")
        st.header("🎉 Final Approved Code")
        st.code(results["final_code"], language="python")
        
        # Display metadata
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Iterations Used", results["iterations_used"])
        with col2:
            st.metric("Max Iterations", results["max_iterations"])
        with col3:
            st.metric("Execution Steps", results["execution_steps"])
            
        # Provide download option
        st.download_button(
            label="📄 Download Code",
            data=results["final_code"],
            file_name="generated_code.py",
            mime="text/python"
        )
    else:
        st.error("❌ The development process failed to generate code. Please try again with a different request.")


def main():
    """Main application function."""
    # Setup page configuration
    setup_page_config()
    
    # Render header
    render_header()
    
    # Check for proper configuration before showing the interface
    try:
        from config import get_llm
        # Test LLM configuration
        get_llm()
        config_ok = True
    except Exception as e:
        config_ok = False
        st.error(f"⚠️ Configuration Error: {str(e)}")
        st.markdown("""
        **To fix this issue:**
        
        **For Local Development:**
        1. Create a `.env` file in the project root
        2. Add your Azure OpenAI credentials:
           ```
           AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=your_deployment_name
           AZURE_OPENAI_CHAT_ENDPOINT=https://your-resource.openai.azure.com/
           AZURE_OPENAI_CHAT_API_KEY=your_api_key
           ```
        
        **For Streamlit Cloud:**
        1. Go to your app's "Manage app" page
        2. Click on "Secrets" tab
        3. Add the credentials in TOML format:
           ```toml
           AZURE_OPENAI_CHAT_DEPLOYMENT_NAME = "your_deployment_name"
           AZURE_OPENAI_CHAT_ENDPOINT = "https://your-resource.openai.azure.com/"
           AZURE_OPENAI_CHAT_API_KEY = "your_api_key"
           ```
        4. Save and restart the app
        """)
        return
    
    if not config_ok:
        return
    
    # Render settings sidebar
    max_iterations = render_settings_sidebar()
    
    # Render input form
    user_request = render_input_form()
    
    # Main action button
    if st.button("🚀 Generate Code", type="primary"):
        if not user_request:
            st.error("Please enter a feature request.")
        else:
            try:
                # Run the development process
                results = run_development_process(user_request, max_iterations)
                
                # Render results
                render_results(results)
                
            except Exception as e:
                st.error(f"An error occurred during the development process: {str(e)}")
                st.exception(e)


if __name__ == "__main__":
    main()
