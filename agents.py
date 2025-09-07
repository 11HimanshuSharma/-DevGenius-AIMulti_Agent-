"""
Agent nodes for DevGenius AI Multi-Agent System.

This module contains all the agent functions that form the nodes of the development workflow graph.
"""

import streamlit as st
from langchain_core.messages import HumanMessage
from models import AgentState
from config import get_llm
from utils import clean_code_response, execute_python_code


def project_manager_node(state: AgentState) -> dict:
    """
    Analyzes the user request and creates a detailed, actionable task.
    
    Args:
        state (AgentState): Current state of the workflow
        
    Returns:
        dict: Updated state with task and messages
    """
    st.write("### 🤵 Project Manager")
    
    with st.spinner("Breaking down the request into a task..."):
        llm = get_llm()
        prompt = f"""
        You are a project manager. Your role is to take a high-level user request and break it down into a clear, concise, and actionable task for a developer.
        The task should be specific and include acceptance criteria.

        User Request: "{state['task']}"

        Create a detailed task description.
        """
        response = llm.invoke(prompt)
        
    st.markdown(f"**Generated Task:**\n```markdown\n{response.content}\n```")
    
    return {
        "task": response.content, 
        "messages": [HumanMessage(content=response.content, name="ProjectManager")]
    }


def developer_node(state: AgentState) -> dict:
    """
    Generates Python code based on the task description.
    
    Args:
        state (AgentState): Current state of the workflow
        
    Returns:
        dict: Updated state with code and messages
    """
    st.write("### 👨‍💻 Developer")
    
    with st.spinner("Writing the first draft of the code..."):
        llm = get_llm()
        prompt = f"""
        You are a senior Python developer. Your task is to write clean, efficient, and well-documented Python code based on the following task description.
        The code should be a single Python script. Do not include any test code in your response, only the functional code.

        Task: "{state['task']}"

        Write the Python code.
        """
        response = llm.invoke(prompt)
        
    clean_code = clean_code_response(response.content)
    st.code(clean_code, language="python")
    
    return {
        "code": clean_code, 
        "messages": [HumanMessage(content=clean_code, name="Developer")]
    }


def reviewer_node(state: AgentState) -> dict:
    """
    Reviews the code for bugs, best practices, and security vulnerabilities.
    
    Args:
        state (AgentState): Current state of the workflow
        
    Returns:
        dict: Updated state with review and messages
    """
    st.write("### 🧐 Code Reviewer")
    
    with st.spinner("Reviewing the code..."):
        llm = get_llm()
        prompt = f"""
        You are a code reviewer. Your task is to review the following Python code for bugs, adherence to best practices, code smells, and potential security vulnerabilities.
        Provide constructive feedback. If the code is good, simply say "No issues found.".

        Code:
        ```python
        {state['code']}
        ```

        Provide your review.
        """
        response = llm.invoke(prompt)
        
    st.markdown(f"**Review:**\n> {response.content}")
    
    return {
        "review": response.content, 
        "messages": [HumanMessage(content=response.content, name="Reviewer")]
    }


def tester_node(state: AgentState) -> dict:
    """
    Generates and executes unit tests for the code.
    
    Args:
        state (AgentState): Current state of the workflow
        
    Returns:
        dict: Updated state with test_results and messages
    """
    st.write("### 🧪 Tester")
    
    with st.spinner("Writing and running tests..."):
        llm = get_llm()
        prompt = f"""
        You are a software tester. Your task is to write unit tests for the following Python code using the `pytest` framework.
        The tests should cover the main functionality and edge cases.
        The code to test is:
        ```python
        {state['code']}
        ```

        Write the pytest test code. Only provide the test code.
        """
        test_code_response = llm.invoke(prompt)
        
    clean_test_code = clean_code_response(test_code_response.content)
    st.code(clean_test_code, language="python")

    # Execute the code and tests
    execution_result = execute_python_code(state['code'], clean_test_code)
    st.markdown(f"**Test Results:**\n```\n{execution_result}\n```")
    
    return {
        "test_results": execution_result, 
        "messages": [HumanMessage(content=execution_result, name="Tester")]
    }


def refactor_node(state: AgentState) -> dict:
    """
    Refactors the code based on review and test feedback.
    
    Args:
        state (AgentState): Current state of the workflow
        
    Returns:
        dict: Updated state with refactored code and incremented iterations
    """
    st.write("### 🛠️ Refactor Agent")
    
    with st.spinner("Refactoring the code based on feedback..."):
        llm = get_llm()
        prompt = f"""
        You are a refactoring expert. Your task is to rewrite the given Python code based on the feedback from the code reviewer and the results from the tester.
        Apply the necessary changes to improve the code.

        Original Code:
        ```python
        {state['code']}
        ```

        Code Review Feedback:
        "{state['review']}"

        Test Results:
        "{state['test_results']}"

        Provide the complete, refactored Python code.
        """
        response = llm.invoke(prompt)
        
    clean_code = clean_code_response(response.content)
    st.code(clean_code, language="python")
    
    return {
        "code": clean_code, 
        "iterations": state['iterations'] + 1
    }
