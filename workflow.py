"""
Workflow management for DevGenius AI Multi-Agent System.

This module contains the graph construction logic and workflow orchestration.
"""

import streamlit as st
from langgraph.graph import StateGraph, END
from models import AgentState
from agents import (
    project_manager_node,
    developer_node,
    reviewer_node,
    tester_node,
    refactor_node
)
from utils import should_continue_development
from config import Config


def should_continue(state: AgentState) -> str:
    """
    Decision point: determines whether to continue refactoring or finish.
    
    Args:
        state (AgentState): Current state of the workflow
        
    Returns:
        str: "end" to finish or "refactor" to continue
    """
    continue_dev, reason = should_continue_development(
        state.get("review", ""),
        state.get("test_results", ""),
        state['iterations'],
        state['max_iterations']
    )
    
    if not continue_dev:
        if "Max iterations" in reason:
            st.warning("Max iterations reached. Exiting.")
        else:
            st.success("Code approved!")
        return "end"
    else:
        st.info("Code requires refactoring. Looping back...")
        return "refactor"


def create_workflow_graph() -> StateGraph:
    """
    Creates and configures the workflow graph for the multi-agent system.
    
    Returns:
        StateGraph: Compiled workflow graph
    """
    # Define the graph
    builder = StateGraph(AgentState)

    # Add nodes
    builder.add_node("project_manager", project_manager_node)
    builder.add_node("developer", developer_node)
    builder.add_node("reviewer", reviewer_node)
    builder.add_node("tester", tester_node)
    builder.add_node("refactor", refactor_node)

    # Define the edges
    builder.set_entry_point("project_manager")
    builder.add_edge("project_manager", "developer")
    builder.add_edge("developer", "reviewer")
    builder.add_edge("reviewer", "tester")
    builder.add_conditional_edges(
        "tester",
        should_continue,
        {
            "refactor": "refactor",
            "end": END
        }
    )
    builder.add_edge("refactor", "reviewer")  # Loop back for another review/test cycle

    # Compile the graph
    return builder.compile()


def run_development_workflow(user_request: str, max_iterations: int = None) -> str:
    """
    Runs the complete development workflow for a given user request.
    
    Args:
        user_request (str): The user's feature request
        max_iterations (int, optional): Maximum number of iterations. Defaults to Config.MAX_ITERATIONS
        
    Returns:
        str: The final approved code
    """
    if max_iterations is None:
        max_iterations = Config.MAX_ITERATIONS
    
    # Create the workflow graph
    graph = create_workflow_graph()
    
    # Run the graph
    initial_state = {
        "task": user_request,
        "iterations": 0,
        "max_iterations": max_iterations,
        "messages": []
    }

    final_state = None
    for s in graph.stream(initial_state):
        # The final state is the last one streamed
        final_state = s

    # Extract the final code
    if final_state:
        final_code = final_state[next(reversed(final_state))].get('code')
        return final_code
    
    return "No code generated"


class WorkflowManager:
    """
    Manages the development workflow and provides additional utilities.
    """
    
    def __init__(self, max_iterations: int = None):
        """
        Initialize the workflow manager.
        
        Args:
            max_iterations (int, optional): Maximum iterations. Defaults to Config.MAX_ITERATIONS
        """
        self.max_iterations = max_iterations or Config.MAX_ITERATIONS
        self.graph = create_workflow_graph()
    
    def execute_workflow(self, user_request: str) -> dict:
        """
        Execute the development workflow and return detailed results.
        
        Args:
            user_request (str): The user's feature request
            
        Returns:
            dict: Workflow execution results including final code and metadata
        """
        initial_state = {
            "task": user_request,
            "iterations": 0,
            "max_iterations": self.max_iterations,
            "messages": []
        }

        final_state = None
        execution_steps = []
        
        for step_state in self.graph.stream(initial_state):
            execution_steps.append(step_state)
            final_state = step_state

        # Extract results
        if final_state:
            final_code = final_state[next(reversed(final_state))].get('code', "")
            iterations_used = final_state[next(reversed(final_state))].get('iterations', 0)
            
            return {
                "final_code": final_code,
                "iterations_used": iterations_used,
                "max_iterations": self.max_iterations,
                "execution_steps": len(execution_steps),
                "success": bool(final_code)
            }
        
        return {
            "final_code": "",
            "iterations_used": 0,
            "max_iterations": self.max_iterations,
            "execution_steps": 0,
            "success": False
        }
