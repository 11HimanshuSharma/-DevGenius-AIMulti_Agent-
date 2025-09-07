"""
Configuration module for DevGenius AI Multi-Agent System.

This module handles environment variables, LLM configuration, and application settings.
"""

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

# Load environment variables from .env file (for local development)
load_dotenv()


class Config:
    """Configuration class to hold all application settings."""
    
    # Azure OpenAI Configuration - handles both local .env and Streamlit secrets
    AZURE_DEPLOYMENT_NAME = (
        st.secrets.get("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME") if hasattr(st, 'secrets') 
        else os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
    )
    AZURE_ENDPOINT = (
        st.secrets.get("AZURE_OPENAI_CHAT_ENDPOINT") if hasattr(st, 'secrets')
        else os.getenv("AZURE_OPENAI_CHAT_ENDPOINT")
    )
    AZURE_API_KEY = (
        st.secrets.get("AZURE_OPENAI_CHAT_API_KEY") if hasattr(st, 'secrets')
        else os.getenv("AZURE_OPENAI_CHAT_API_KEY")
    )
    AZURE_API_VERSION = "2024-12-01-preview"
    
    # LLM Configuration
    TEMPERATURE = 0
    MAX_TOKENS = None
    TIMEOUT = None
    MAX_RETRIES = 2
    
    # Application Settings
    MAX_ITERATIONS = 3
    CODE_EXECUTION_TIMEOUT = 30


def get_llm() -> AzureChatOpenAI:
    """
    Initialize and return the Azure OpenAI LLM instance.
    
    Returns:
        AzureChatOpenAI: Configured LLM instance
    """
    return AzureChatOpenAI(
        azure_deployment=Config.AZURE_DEPLOYMENT_NAME,
        azure_endpoint=Config.AZURE_ENDPOINT,
        api_key=Config.AZURE_API_KEY,
        api_version=Config.AZURE_API_VERSION,
        temperature=Config.TEMPERATURE,
        max_tokens=Config.MAX_TOKENS,
        timeout=Config.TIMEOUT,
        max_retries=Config.MAX_RETRIES,
    )
