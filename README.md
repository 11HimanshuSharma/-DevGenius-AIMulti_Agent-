<!-- @format -->

# DevGenius AI Multi-Agent System

A modular Streamlit application that simulates a team of AI agents collaborating
to write, review, test, and refine code based on user requests.

## 🏗️ Project Structure

```
📦 DevGenius
├── 📄 app.py                 # Main Streamlit application (UI layer)
├── 📄 config.py              # Configuration and environment setup
├── 📄 models.py              # Data models and type definitions
├── 📄 agents.py              # AI agent implementations
├── 📄 workflow.py            # Workflow orchestration and graph logic
├── 📄 utils.py               # Utility functions and helpers
├── 📄 requirements.txt       # Python dependencies
└── 📄 README.md              # Project documentation
```

## 🤖 Agents

The system consists of 5 specialized AI agents:

- **🤵 Project Manager**: Analyzes user requests and creates detailed,
  actionable tasks
- **👨‍💻 Developer**: Writes clean, efficient Python code based on requirements
- **🧐 Code Reviewer**: Reviews code for bugs, best practices, and security
  issues
- **🧪 Tester**: Creates and executes unit tests using pytest
- **🛠️ Refactor Agent**: Improves code based on review and test feedback

## 📋 Features

- **Modular Architecture**: Clean separation of concerns with dedicated modules
- **Interactive UI**: Streamlit-based interface with real-time feedback
- **Configurable Settings**: Adjustable iteration limits and parameters
- **Code Download**: Export generated code as Python files
- **Error Handling**: Robust error handling and user feedback
- **Environment Management**: Secure environment variable handling

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Azure OpenAI API access
- Required environment variables (see Configuration)

### Installation

1. **Clone or download the project files**

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (create a `.env` file):

   ```env
   AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=your_deployment_name
   AZURE_OPENAI_CHAT_ENDPOINT=your_endpoint_url
   AZURE_OPENAI_CHAT_API_KEY=your_api_key
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

## ⚙️ Configuration

The application can be configured through the `config.py` file:

- **LLM Settings**: Temperature, max tokens, timeout, retries
- **Application Settings**: Max iterations, execution timeout
- **Azure OpenAI**: Deployment details and API configuration

## 📁 Module Details

### `app.py` - Main Application

- Streamlit UI components
- User interaction handling
- Results display and formatting
- Settings sidebar

### `config.py` - Configuration

- Environment variable management
- LLM initialization
- Application settings

### `models.py` - Data Models

- `AgentState`: Workflow state management
- `TaskRequest`: User input validation
- `CodeExecutionResult`: Execution results
- `AgentResponse`: Agent communication

### `agents.py` - AI Agents

- Individual agent implementations
- LLM prompt templates
- Agent-specific logic

### `workflow.py` - Workflow Management

- LangGraph workflow construction
- State transitions and decisions
- Execution orchestration

### `utils.py` - Utilities

- Code execution and testing
- String processing helpers
- Workflow decision logic

## 🔄 Workflow Process

1. **Project Manager** analyzes the user request
2. **Developer** creates initial code implementation
3. **Code Reviewer** examines code quality and best practices
4. **Tester** generates and runs unit tests
5. **Decision Point**: Continue refactoring or approve final code
6. **Refactor Agent** (if needed) improves code based on feedback
7. **Loop** back to review until code is approved or max iterations reached

## 🛠️ Customization

### Adding New Agents

1. Create agent function in `agents.py`
2. Add node to workflow in `workflow.py`
3. Update state model in `models.py` if needed

### Modifying Workflow

1. Update graph construction in `workflow.py`
2. Modify decision logic in `utils.py`
3. Adjust UI feedback in `app.py`

### Changing LLM Provider

1. Update imports and configuration in `config.py`
2. Modify agent implementations in `agents.py`
3. Test with new provider

## 📊 Best Practices Implemented

- **Separation of Concerns**: Each module has a single responsibility
- **Type Hints**: Full type annotation for better code quality
- **Error Handling**: Comprehensive error handling and user feedback
- **Documentation**: Detailed docstrings and comments
- **Configuration Management**: Centralized configuration
- **Modular Design**: Easy to extend and maintain

## 🤝 Contributing

1. Follow the existing code structure and patterns
2. Add type hints to all functions
3. Include docstrings for public functions
4. Test changes thoroughly
5. Update documentation as needed

## 📝 License

This project is for educational and development purposes.

## 🔧 Troubleshooting

### Common Issues

1. **Environment Variables**: Ensure `.env` file is properly configured
2. **Dependencies**: Run `pip install -r requirements.txt` to install all
   dependencies
3. **Azure OpenAI**: Verify API key and endpoint are correct
4. **Pytest**: Ensure pytest is installed for code testing functionality

### Getting Help

- Check the console output for detailed error messages
- Verify environment variable configuration
- Ensure all dependencies are installed correctly
