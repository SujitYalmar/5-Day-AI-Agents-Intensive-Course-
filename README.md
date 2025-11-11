# 🤖 AI Agent Development with Google ADK

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

> **Building Intelligent AI Agents using Google's Agent Development Kit (ADK)**
>
> A comprehensive implementation of AI agents powered by Google's Gemini models, featuring Google Search integration and multi-agent architectures.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project demonstrates the development of AI agents using Google's **Agent Development Kit (ADK)**. Unlike traditional LLMs that simply respond to prompts, these agents can:

- **Think**: Reason about problems and plan actions
- **Act**: Use tools like Google Search to gather information
- **Observe**: Learn from results and refine responses

The project is based on Kaggle's 5-day Agents course and includes practical examples of building both simple and multi-agent systems.

## ✨ Features

- 🚀 **Simple Agent Implementation**: Basic agent with Google Search integration
- 🔧 **Tool Integration**: Seamless integration with Google Search and other tools
- 🎨 **ADK Web UI**: Interactive web interface for testing and debugging agents
- 📊 **Multi-Agent Architecture**: Examples of complex agent workflows
- 🔑 **Secure API Management**: Best practices for handling API keys
- 📝 **Comprehensive Documentation**: Step-by-step guides and examples

## 🛠️ Prerequisites

Before you begin, ensure you have:

- **Python 3.11+** installed
- **Google API Key** from [Google AI Studio](https://aistudio.google.com/app/api-keys)
- Basic understanding of Python and AI concepts

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SujitYalmar/AI-Agent-Development-ADK.git
cd AI-Agent-Development-ADK
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\\Scripts\\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
GOOGLE_API_KEY=your_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

## 🚀 Quick Start

### Running Your First Agent

```python
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search

# Define your agent
agent = Agent(
    name="helpful_assistant",
    model="gemini-2.5-flash-lite",
    description="A simple agent that can answer general questions.",
    instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
    tools=[google_search],
)

# Create a runner
runner = InMemoryRunner(agent=agent)

# Run a query
response = await runner.run_debug("What is Agent Development Kit from Google?")
print(response)
```

### Launching the ADK Web UI

```bash
# Create a sample agent
adk create sample-agent --model gemini-2.5-flash-lite --api_key $GOOGLE_API_KEY

# Start the web interface
adk web
```

Then open your browser to `http://127.0.0.1:8000`

## 📁 Project Structure

```
AI-Agent-Development-ADK/
├── README.md                 # This file
├── LICENSE                   # Apache 2.0 License
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
├── notebooks/               # Jupyter notebooks
│   └── day_1a_from_prompt_to_action.ipynb
├── src/                     # Source code
│   ├── __init__.py
│   ├── agent.py            # Main agent implementation
│   └── config.py           # Configuration management
├── examples/               # Example scripts
│   ├── simple_agent.py
│   └── multi_agent.py
└── docs/                   # Additional documentation
    ├── setup_guide.md
    └── api_reference.md
```

## 💡 Usage Examples

### Example 1: Weather Query Agent

```python
response = await runner.run_debug("What's the weather in London?")
```

### Example 2: Information Research Agent

```python
response = await runner.run_debug(
    "What are the key features of Google's Agent Development Kit?"
)
```

### Example 3: Custom Tool Integration

```python
from google.adk.tools import Tool

# Define custom tool
@Tool
def calculator(expression: str) -> float:
    """Evaluates mathematical expressions."""
    return eval(expression)

# Add to agent
agent = Agent(
    name="math_agent",
    model="gemini-2.5-flash-lite",
    tools=[calculator, google_search],
)
```

## 📚 Documentation

### Official ADK Resources

- [ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Quickstart for Python](https://google.github.io/adk-docs/get-started/python/)
- [ADK Agents Overview](https://google.github.io/adk-docs/agents/)
- [ADK Tools Overview](https://google.github.io/adk-docs/tools/)

### Course Resources

- [Kaggle 5-Day Agents Course](https://www.kaggle.com/learn/agents)
- [Kaggle Discord Community](https://discord.com/invite/kaggle)

## 🔧 Configuration

### API Key Management

**Never commit API keys to version control!**

- Use environment variables
- Store keys in `.env` files (included in `.gitignore`)
- For Kaggle Notebooks, use Kaggle Secrets

### Model Selection

Available Gemini models:
- `gemini-2.5-flash-lite` (recommended for testing)
- `gemini-2.5-pro`
- `gemini-1.5-flash`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google's Agent Development Kit team
- Kaggle for the comprehensive Agents course
- The AI and machine learning community

## 📧 Contact

**Sujit Yalmar**
- GitHub: [@SujitYalmar](https://github.com/SujitYalmar)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)

---

⭐ **If you find this project helpful, please consider giving it a star!** ⭐

---

*Last Updated: November 2025*
