"""
Data models for DevGenius AI Multi-Agent System.

This module contains all the data structures and type definitions used throughout the application.
"""

from typing import TypedDict, Annotated, List
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    """
    Represents the state of our multi-agent system.
    
    This state is passed between agents and contains all the information
    needed for the development workflow.
    """
    task: str                # The task description from the project manager
    code: str                # The current code being developed
    review: str              # Code review feedback
    test_results: str        # Results from test execution
    iterations: int          # Current iteration count
    max_iterations: int      # Maximum allowed iterations
    final_code: str          # The final approved code
    messages: Annotated[List[BaseMessage], lambda x, y: x + y]  # Message history


class TaskRequest(BaseModel):
    """
    Model for incoming task requests.
    """
    description: str = Field(..., description="The task description provided by the user")
    max_iterations: int = Field(default=3, description="Maximum number of refinement iterations")


class CodeExecutionResult(BaseModel):
    """
    Model for code execution results.
    """
    success: bool = Field(..., description="Whether the execution was successful")
    output: str = Field(..., description="The output from code execution")
    error: str = Field(default="", description="Error message if execution failed")


class AgentResponse(BaseModel):
    """
    Model for agent responses.
    """
    agent_name: str = Field(..., description="Name of the agent providing the response")
    content: str = Field(..., description="The response content")
    success: bool = Field(default=True, description="Whether the operation was successful")
