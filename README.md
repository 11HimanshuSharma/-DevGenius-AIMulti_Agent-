<!-- @format -->

# 🤖 DevGenius: AI Multi-Agent Development Team

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**A sophisticated AI multi-agent system that simulates a complete software
development team, automating the entire code development lifecycle from
requirements analysis to final implementation.**

## 🎯 Problem Statement

### The Challenge

Software development is a complex, multi-stage process that traditionally
requires diverse expertise:

- **Requirements Analysis**: Understanding and breaking down user needs
- **Code Development**: Writing clean, efficient implementations
- **Code Review**: Ensuring quality, security, and best practices
- **Testing**: Creating comprehensive test suites and validation
- **Refactoring**: Iterative improvement based on feedback

Currently, individual developers or small teams must handle all these
responsibilities, leading to:

- **Knowledge Gaps**: Not everyone excels in all areas (testing, security,
  architecture)
- **Time Constraints**: Manual process is slow and error-prone
- **Inconsistent Quality**: Human oversight limitations
- **Scalability Issues**: Hard to maintain quality across large projects

### Why AI Multi-Agent Systems?

This problem is **perfectly suited for AI multi-agent collaboration** because:

1. **Specialized Expertise**: Each agent can be optimized for specific domains
   (testing, security, code quality)
2. **Parallel Processing**: Multiple agents can work simultaneously on different
   aspects
3. **Consistent Quality**: AI agents don't suffer from fatigue or oversight
4. **Iterative Improvement**: Agents can collaborate through multiple refinement
   cycles
5. **Scalability**: System can handle multiple projects simultaneously
6. **Knowledge Aggregation**: Combines best practices from vast training
   datasets

### Unique Value of Multi-Agent Collaboration

- **Domain Specialization**: Each agent has focused expertise and specialized
  prompting
- **Quality Assurance**: Multiple perspectives ensure comprehensive coverage
- **Automated Workflow**: Seamless handoffs between development stages
- **Continuous Feedback Loop**: Iterative improvement through agent
  collaboration
- **Consistency**: Standardized processes across all projects

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

## 🏗️ Project Architecture

### Multi-Agent Workflow

```
User Request → Project Manager → Developer → Code Reviewer → Tester
                                                ↓
Final Code ← Refactor Agent ←←←← Decision Point ←←↓
     ↑                           ↓
     ←←←←← (Loop if needed) ←←←←←↓
```

### 🤖 Agent Specifications

#### 🤵 **Project Manager Agent**

- **Role**: Requirements analysis and task decomposition
- **Input**: Raw user requests
- **Output**: Structured, actionable task descriptions
- **Specialty**: Business analysis, scope definition, acceptance criteria

#### 👨‍💻 **Developer Agent**

- **Role**: Code implementation and architecture
- **Input**: Detailed task specifications
- **Output**: Clean, functional Python code
- **Specialty**: Software design patterns, code structure, best practices

#### 🧐 **Code Reviewer Agent**

- **Role**: Quality assurance and security analysis
- **Input**: Generated code
- **Output**: Comprehensive review feedback
- **Specialty**: Security vulnerabilities, performance optimization, code
  quality

#### 🧪 **Tester Agent**

- **Role**: Test creation and validation
- **Input**: Code implementation
- **Output**: pytest test suites and execution results
- **Specialty**: Test-driven development, edge case identification, coverage
  analysis

#### 🛠️ **Refactor Agent**

- **Role**: Code improvement and integration
- **Input**: Code + Review feedback + Test results
- **Output**: Refined, production-ready code
- **Specialty**: Code optimization, issue resolution, quality enhancement

### Agent Interaction Protocol

- **State Management**: Shared state object tracks all artifacts
- **Sequential Processing**: Ordered agent execution with feedback loops
- **Quality Gates**: Automated decision points for workflow continuation
- **Iterative Refinement**: Multiple improvement cycles until approval

## 🛠️ Technology Stack

### **Core Frameworks**

- **LangGraph**: Multi-agent workflow orchestration
- **LangChain**: LLM integration and agent foundation
- **Streamlit**: Interactive web application framework
- **Pydantic**: Data validation and configuration management

### **LLM Integration**

- **Primary**: Azure OpenAI (GPT-4/GPT-4 Turbo)
- **Alternative**: OpenAI GPT-3.5 Turbo
- **Free Options**: Google Gemini Pro, Hugging Face models
- **Framework**: langchain-openai for seamless integration

### **Development Tools**

- **Testing**: pytest for automated test execution
- **Environment**: python-dotenv for configuration
- **Data Processing**: NumPy, Pandas for generated scripts

## 🧠 LLM Selection Analysis

### **Primary Choice: GPT-4 / GPT-4 Turbo**

#### **Why GPT-4?**

- **Superior Code Generation**: Exceptional Python programming capabilities
- **Advanced Reasoning**: Complex code analysis and security review
- **Consistency**: Reliable output quality across all agents
- **Professional Quality**: Production-ready code generation
- **Integration**: Mature Azure OpenAI service with enterprise SLA

#### **Technical Specifications**

```python
MODEL_CONFIG = {
    "model": "gpt-4-turbo",
    "temperature": 0,        # Deterministic outputs
    "max_tokens": 4096,      # Sufficient for complex code
    "context_window": "128K", # Large context support
}
```

### **Free-Tier Options**

#### **🆓 OpenAI GPT-3.5 Turbo** (Recommended Budget Option)

- **Cost**: $0.002/1K tokens (very affordable)
- **Performance**: 70-80% of GPT-4 quality
- **Speed**: Faster response times
- **Use Case**: Development, testing, educational demos

#### **🆓 Google Gemini Pro**

- **Cost**: Generous free tier quotas
- **Quality**: Competitive code generation
- **Integration**: Available via Vertex AI
- **Use Case**: Public demos, experimentation

#### **🆓 Open Source Models** (Hugging Face)

- **Options**: Code Llama, StarCoder, Mistral
- **Cost**: Completely free (requires infrastructure)
- **Control**: Full customization and privacy
- **Use Case**: Research, on-premises deployment

### **Model Selection Justification**

**For Production**: GPT-4 provides the reliability and quality needed for
business applications.

**For Development**: GPT-3.5 Turbo offers excellent value for testing and
iteration.

**For Education**: Gemini Pro's free tier makes it perfect for demonstrations
and learning.

## 📚 Detailed Documentation

- **[Project Overview](PROJECT_OVERVIEW.md)**: Comprehensive application
  description
- **[Agent Architecture](AGENT_ARCHITECTURE.md)**: Detailed agent interactions
  and workflows
- **[Technology Stack](TECHNOLOGY_STACK.md)**: Complete framework and tool
  analysis
- **[LLM Analysis](LLM_ANALYSIS.md)**: In-depth LLM selection and comparison
- **[Deployment Guide](DEPLOYMENT.md)**: Step-by-step deployment instructions

## 🏗️ Project Structure

```
📦 DevGenius
├── 📄 app.py                     # Main Streamlit application (UI layer)
├── 📄 config.py                  # Configuration and environment setup
├── 📄 models.py                  # Data models and type definitions
├── 📄 agents.py                  # AI agent implementations
├── 📄 workflow.py                # Workflow orchestration and graph logic
├── 📄 utils.py                   # Utility functions and helpers
├── 📄 requirements.txt           # Python dependencies
├── 📄 .streamlit/config.toml     # Streamlit configuration
├── 📄 .env.example               # Environment variables template
├── 📄 DEPLOYMENT.md              # Deployment instructions
├── 📄 DEPLOYMENT_CHECKLIST.md    # Step-by-step deployment guide
└── 📄 README.md                  # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Azure OpenAI API access (or alternative LLM provider)
- Git for version control

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/11HimanshuSharma/-DevGenius-AIMulti_Agent-.git
   cd DevGenius-AIMulti_Agent
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (copy `.env.example` to `.env`):

   ```env
   AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=your_deployment_name
   AZURE_OPENAI_CHAT_ENDPOINT=https://your-resource.openai.azure.com/
   AZURE_OPENAI_CHAT_API_KEY=your_api_key
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

### Quick Start Example

1. Open the application in your browser
2. Enter a request: "Create a function to calculate fibonacci numbers"
3. Adjust settings in the sidebar (optional)
4. Click "🚀 Generate Code"
5. Watch the AI team collaborate in real-time
6. Download your production-ready code!

## 🌐 Live Demo

🔗 **Deployed Application**:
[DevGenius on Streamlit Cloud](https://your-app-name.streamlit.app)

_Try it yourself! The demo includes all features and showcases the complete
multi-agent workflow._

````

4. **Run the application**:
```bash
streamlit run app.py
````

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
