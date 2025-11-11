# 🤖 AI Agent Development with Google ADK

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/SujitYalmar/AI-Agent-Development-ADK?style=social)](https://github.com/SujitYalmar/AI-Agent-Development-ADK/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/SujitYalmar/AI-Agent-Development-ADK)](https://github.com/SujitYalmar/AI-Agent-Development-ADK/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/SujitYalmar/AI-Agent-Development-ADK)](https://github.com/SujitYalmar/AI-Agent-Development-ADK/commits/main)

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
- - [FAQ](#faq)
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

## ❓ FAQ

### How do I get a Google API key for Gemini models?

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key
5. Add it to your `.env` file as `GOOGLE_API_KEY=your_key_here`

**Security Note:** Never commit API keys to version control!

### What Python version do I need?

Python 3.11 or higher is required. Check your version:

```bash
python --version
```

### How do I run the examples on Kaggle?

1. Upload the notebook to Kaggle
2. Enable internet access in notebook settings
3. Add your Google API key to Kaggle Secrets:
   - Go to "Add-ons" → "Secrets"
   - Add key: `GOOGLE_API_KEY`
   - Value: your API key
4. Run the cells

### The agent isn't responding. What should I check?

**Common issues:**

1. **API Key Issues:**
   - Verify your API key is correct
   - Check if the key has permissions
   - Ensure `.env` file is in the correct location

2. **Network Issues:**
   - Check your internet connection
   - Verify firewall settings
   - Try with a VPN if restricted

3. **Code Issues:**
   - Check for syntax errors
   - Verify all dependencies are installed
   - Review error messages in console

### How can I customize the agent's behavior?

You can customize various aspects:

```python
# Change the model
agent = Agent(
    model="gemini-1.5-pro",  # or "gemini-1.5-flash"
)

# Add system instructions
agent = Agent(
    model="gemini-1.5-flash",
    system_instruction="You are a helpful coding assistant"
)

# Customize tools
agent = Agent(
    model="gemini-1.5-flash",
    tools=[GoogleSearch(), CustomTool()]
)
```

### How do I add custom tools to my agent?

Create a custom tool by extending the base tool class:

```python
from google.adk.tools import Tool

class MyCustomTool(Tool):
    def __init__(self):
        super().__init__(
            name="my_tool",
            description="What this tool does"
        )
    
    def execute(self, **kwargs):
        # Your custom logic here
        return result

# Use it in your agent
agent = Agent(
    model="gemini-1.5-flash",
    tools=[MyCustomTool()]
)
```

### Can I use this in production?

Yes, but consider:

- **Rate Limits:** Check Google's API quotas
- **Error Handling:** Implement robust error handling
- **Monitoring:** Add logging and monitoring
- **Security:** Never expose API keys
- **Testing:** Thoroughly test all scenarios
- **Costs:** Monitor API usage and costs

### How do I contribute to this project?

We welcome contributions! See our [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Code of conduct
- Development setup
- Pull request process
- Coding standards

### Where can I get help?

- **Issues:** [GitHub Issues](https://github.com/SujitYalmar/AI-Agent-Development-ADK/issues)
- **Discussions:** [GitHub Discussions](https://github.com/SujitYalmar/AI-Agent-Development-ADK/discussions)
- **Documentation:** Check the [Google ADK docs](https://ai.google.dev/adk)
- **Examples:** Review the `examples/` folder

### What's the difference between gemini-1.5-pro and gemini-1.5-flash?

| Feature | Gemini 1.5 Pro | Gemini 1.5 Flash |
|---------|----------------|------------------|
| **Speed** | Slower | Faster |
| **Cost** | Higher | Lower |
| **Performance** | Better for complex tasks | Good for simple tasks |
| **Context Window** | Larger | Smaller |
| **Best For** | Complex reasoning, analysis | Quick responses, simple tasks |

### How do I handle rate limiting?

Implement retry logic with exponential backoff:

```python
import time
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
async def run_agent_with_retry(agent, query):
    return await agent.run(query)
```

### Can I use multiple agents together?

Yes! You can create multi-agent systems:

```python
# Create specialized agents
researcher = Agent(model="gemini-1.5-pro", tools=[GoogleSearch()])
writer = Agent(model="gemini-1.5-flash")

# Coordinate between agents
research_result = await researcher.run("Research topic X")
final_output = await writer.run(f"Write article based on: {research_result}")
```

---

*Last Updated: November 2025*
