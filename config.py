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


def get_config_value(key: str) -> str:
    """
    Get configuration value from either Streamlit secrets or environment variables.
    
    Args:
        key: Configuration key name
        
    Returns:
        Configuration value or None if not found
    """
    # Try Streamlit secrets first (for cloud deployment)
    try:
        if hasattr(st, 'secrets') and st.secrets:
            return st.secrets.get(key)
    except Exception:
        pass
    
    # Fall back to environment variables (for local development)
    return os.getenv(key)


class Config:
    """Configuration class to hold all application settings."""
    
    # Azure OpenAI Configuration - handles both local .env and Streamlit secrets
    @property
    def AZURE_DEPLOYMENT_NAME(self) -> str:
        return get_config_value("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
    
    @property  
    def AZURE_ENDPOINT(self) -> str:
        return get_config_value("AZURE_OPENAI_CHAT_ENDPOINT")
    
    @property
    def AZURE_API_KEY(self) -> str:
        return get_config_value("AZURE_OPENAI_CHAT_API_KEY")
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
        
    Raises:
        ValueError: If required credentials are missing or invalid
    """
    config = Config()
    
    # Validate that all required credentials are present
    if not config.AZURE_DEPLOYMENT_NAME:
        raise ValueError("Missing AZURE_OPENAI_CHAT_DEPLOYMENT_NAME. Please check your environment variables or Streamlit secrets.")
    
    if not config.AZURE_ENDPOINT:
        raise ValueError("Missing AZURE_OPENAI_CHAT_ENDPOINT. Please check your environment variables or Streamlit secrets.")
        
    if not config.AZURE_API_KEY:
        raise ValueError("Missing AZURE_OPENAI_CHAT_API_KEY. Please check your environment variables or Streamlit secrets.")
    
    # Validate endpoint format
    if not config.AZURE_ENDPOINT.startswith('https://'):
        raise ValueError(f"Invalid endpoint format: {config.AZURE_ENDPOINT}. Should start with 'https://' and be your base Azure endpoint (not the full completion URL).")
    
    # Validate deployment name (should not be a URL)
    if config.AZURE_DEPLOYMENT_NAME.startswith('http'):
        raise ValueError(f"Invalid deployment name: {config.AZURE_DEPLOYMENT_NAME}. Should be just the deployment name (e.g., 'gpt-4o-2'), not a URL.")
    
    try:
        return AzureChatOpenAI(
            azure_deployment=config.AZURE_DEPLOYMENT_NAME,
            azure_endpoint=config.AZURE_ENDPOINT,
            api_key=config.AZURE_API_KEY,
            api_version=Config.AZURE_API_VERSION,
            temperature=Config.TEMPERATURE,
            max_tokens=Config.MAX_TOKENS,
            timeout=Config.TIMEOUT,
            max_retries=Config.MAX_RETRIES,
        )
    except Exception as e:
        raise ValueError(f"Failed to initialize Azure OpenAI client. Please check your credentials. Error: {str(e)}")
