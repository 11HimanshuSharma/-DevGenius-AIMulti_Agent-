"""
Utility functions for DevGenius AI Multi-Agent System.

This module contains helper functions for code execution, file handling, and other utilities.
"""

import os
import subprocess
import tempfile
from typing import Tuple
from models import CodeExecutionResult
from config import Config


def execute_python_code(code: str, test_code: str) -> str:
    """
    Executes Python code with corresponding tests in a temporary file and returns the result.
    
    Args:
        code (str): The Python code to execute
        test_code (str): The test code to run against the main code
        
    Returns:
        str: The execution result including test output and any errors
    """
    code_file_path = None
    test_file_path = None
    
    try:
        # Create temporary files for code and tests
        with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".py") as code_file:
            code_file.write(code)
            code_file_path = code_file.name

        with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix="_test.py") as test_file:
            test_file.write(test_code)
            test_file_path = test_file.name

        # Run pytest
        process = subprocess.run(
            ["pytest", test_file_path],
            capture_output=True,
            text=True,
            timeout=Config.CODE_EXECUTION_TIMEOUT
        )
        
        if process.returncode == 0:
            return f"All tests passed!\nOutput:\n{process.stdout}"
        else:
            return f"Tests failed.\nStdout:\n{process.stdout}\nStderr:\n{process.stderr}"
            
    except subprocess.TimeoutExpired:
        return "Execution timed out."
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        # Clean up temporary files
        if code_file_path and os.path.exists(code_file_path):
            os.remove(code_file_path)
        if test_file_path and os.path.exists(test_file_path):
            os.remove(test_file_path)


def clean_code_response(response_content: str) -> str:
    """
    Cleans up code response by removing markdown formatting.
    
    Args:
        response_content (str): Raw response content from LLM
        
    Returns:
        str: Cleaned code without markdown fences
    """
    return response_content.strip().replace("```python", "").replace("```", "").strip()


def should_continue_development(review: str, test_results: str, iterations: int, max_iterations: int) -> Tuple[bool, str]:
    """
    Determines whether the development process should continue or end.
    
    Args:
        review (str): Code review feedback
        test_results (str): Test execution results
        iterations (int): Current iteration count
        max_iterations (int): Maximum allowed iterations
        
    Returns:
        Tuple[bool, str]: (should_continue, reason)
    """
    if iterations >= max_iterations:
        return False, "Max iterations reached"
    
    review_lower = review.lower()
    test_results_lower = test_results.lower()
    
    if "no issues found" in review_lower and "tests failed" not in test_results_lower and "error" not in test_results_lower:
        return False, "Code approved - no issues found and all tests passed"
    else:
        return True, "Code requires refactoring based on review or test feedback"


def format_agent_output(agent_name: str, content: str, content_type: str = "markdown") -> str:
    """
    Formats agent output for consistent display.
    
    Args:
        agent_name (str): Name of the agent
        content (str): Content to format
        content_type (str): Type of content (markdown, code, etc.)
        
    Returns:
        str: Formatted content string
    """
    if content_type == "code":
        return f"**{agent_name} Output:**\n```python\n{content}\n```"
    elif content_type == "review":
        return f"**{agent_name} Review:**\n> {content}"
    else:
        return f"**{agent_name}:**\n{content}"
