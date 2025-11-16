# 🚀 5-Day AI Agents Intensive Course

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Google ADK](https://img.shields.io/badge/Google-ADK-red.svg)](https://github.com/googleapis/python-client-libraries)
[![Gemini](https://img.shields.io/badge/Gemini-Models-orange.svg)](https://gemini.google.com/)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](#)

**Master AI Agent Development with Google's Agent Development Kit (ADK) & Gemini Models**

[Overview](#overview) • [Quick Start](#quick-start) • [Course Structure](#course-structure) • [Learning Outcomes](#learning-outcomes) • [Contributing](#contributing)

</div>

---

## 📚 Overview

A comprehensive, hands-on repository containing all materials from the **5-Day AI Agents Intensive Course** by **Google × Kaggle**. This course takes you from agent fundamentals to production-ready deployment.

### What You'll Find Here

✅ **5 Day-by-Day Learning Paths** — Progressive, structured curriculum  
✅ **Interactive Jupyter Notebooks** — Codelabs with executable examples  
✅ **Production-Ready Code** — Tools, templates, and utilities  
✅ **Whitepapers & References** — PDF summaries and research materials  
✅ **Multi-Agent Workflows** — Complex system design patterns  
✅ **Deployment Templates** — Ready to deploy on Vertex AI Agent Engine

---

## 📖 Table of Contents

- [Quick Start](#quick-start)
- [Course Structure](#course-structure)
- [Project Layout](#project-layout)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Learning Outcomes](#learning-outcomes)
- [Usage Guide](#usage-guide)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## Quick Start

### Clone & Setup (5 minutes)

```bash
# 1. Clone the repository
git clone https://github.com/SujitYalmar/5-Day-AI-Agents-Intensive-Course-.git
cd 5-Day-AI-Agents-Intensive-Course-

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# OR .\venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY

# 5. Launch Jupyter
jupyter notebook

# 6. Start with Day-1 notebooks!
```

---

## 📅 Course Structure

| Day | Topic | Focus Area | Duration |
|-----|-------|-----------|----------|
| **Day 1** | 🧠 Introduction to Agents | Foundations & taxonomy of AI agents | 6 hours |
| **Day 2** | 🔧 Tools & Interoperability | Agent tools, APIs, Model Context Protocol (MCP) | 6 hours |
| **Day 3** | 💾 Context Engineering | Sessions, working memory, long-term memory | 6 hours |
| **Day 4** | 📊 Agent Quality & Observability | Logs, traces, metrics, LLM-as-a-Judge evaluation | 6 hours |
| **Day 5** | 🚀 Prototype to Production | A2A Protocols, deployment, scaling | 6 hours |

### Each Day Includes

- 📝 **Summary Notes** — Key concepts and takeaways
- 💻 **Codelabs** — Hands-on Google-provided tutorials
- 🔬 **Practice Code** — Exercises to reinforce learning
- 📄 **Whitepapers** — PDF references and research papers

---

## 📁 Project Layout

```
5-Day-AI-Agents-Intensive-Course-/
│
├── Day-1_intro_to_agents/              # Agent fundamentals & taxonomy
│   ├── notebooks/
│   ├── codelabs/
│   └── summary_notes.md
│
├── Day-2_agent_architecture/           # Tools & MCP integration
│   ├── notebooks/
│   ├── tool_examples/
│   └── mcp_protocols.md
│
├── Day-3_tools_and_memory/             # Memory & context systems
│   ├── notebooks/
│   ├── memory_patterns/
│   └── session_management.md
│
├── Day-4_evaluation_and_scaling/       # Quality metrics & evaluation
│   ├── notebooks/
│   ├── evaluation_tools/
│   └── observability_guide.md
│
├── Day-5_evaluation_and_scaling/       # Production deployment
│   ├── notebooks/
│   ├── deployment_templates/
│   └── a2a_protocols.md
│
├── Tools/                              # Reusable utilities & helpers
│   ├── cost_estimation.py
│   ├── agent_templates.py
│   └── README.md
│
├── Whitepapers/                        # Research & reference materials
│   ├── agent_architecture.pdf
│   ├── memory_systems.pdf
│   └── evaluation_metrics.pdf
│
├── examples/                           # End-to-end project examples
│   ├── simple_agent.ipynb
│   ├── multi_agent_system.ipynb
│   └── deployment_example.ipynb
│
├── .env.example                        # Environment template
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
├── CONTRIBUTING.md                     # Contribution guidelines
└── LICENSE                             # Apache 2.0 License
```

---

## 📋 Prerequisites

**System Requirements:**
- Python 3.8 or higher
- pip (Python package manager)
- 4GB RAM minimum
- 500MB disk space

**Required Knowledge:**
- Basic Python programming
- Familiarity with Jupyter notebooks
- Basic understanding of LLMs/AI concepts (helpful but not required)

**External Services:**
- Google Cloud account (for Gemini API access)
- Optional: Vertex AI account (for deployment examples)

---

## 🛠️ Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/SujitYalmar/5-Day-AI-Agents-Intensive-Course-.git
cd 5-Day-AI-Agents-Intensive-Course-
```

### Step 2: Create Virtual Environment

```bash
python -m venv .venv

# Activate (choose your OS):
source .venv/bin/activate      # macOS/Linux
.\venv\Scripts\activate         # Windows
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```env
GOOGLE_API_KEY=your_api_key_here
PROJECT_ID=your_gcp_project_id
VERTEX_AI_LOCATION=us-central1
```

### Step 5: Verify Installation

```bash
jupyter notebook
# Open http://localhost:8888 in your browser
```

---

## 🎯 Learning Outcomes

After completing this course, you will:

### Day 1 - Foundation
- ✅ Understand modern AI agent architecture and design patterns
- ✅ Know the difference between reactive, planning, and hybrid agents
- ✅ Learn agent lifecycle and state management

### Day 2 - Tools & Integration
- ✅ Extend agent capabilities using tools and APIs
- ✅ Implement Model Context Protocol (MCP) for standardization
- ✅ Build custom tool connectors

### Day 3 - Intelligence
- ✅ Design session-aware systems
- ✅ Implement working and long-term memory
- ✅ Engineer context windows for optimal performance

### Day 4 - Quality
- ✅ Debug agents using traces and logs
- ✅ Measure agent performance with custom metrics
- ✅ Evaluate agents using LLM-as-a-Judge

### Day 5 - Production
- ✅ Deploy agents on Vertex AI Agent Engine
- ✅ Scale multi-agent systems
- ✅ Implement A2A (Agent-to-Agent) protocols
- ✅ Monitor and maintain production systems

---

## 💡 Usage Guide

### For Beginners

1. Start with **Day-1_intro_to_agents**
2. Read the `summary_notes.md` first
3. Run notebooks sequentially
4. Complete all codelabs
5. Progress to Day 2

### For Experienced Developers

1. Review **SUMMARY.md** for quick reference
2. Jump to specific days based on interests
3. Explore the **Tools** directory
4. Run **examples** for reference implementations

### Running a Notebook

```bash
# From the repo root
jupyter notebook Day-1_intro_to_agents/

# Select and open a notebook file (.ipynb)
# Run cells sequentially (Shift + Enter)
```

### Common Workflows

**Build a Simple Agent:**
```python
from Day-1_intro_to_agents import SimpleAgent

agent = SimpleAgent(model="gemini-pro")
response = agent.run("Hello, tell me about AI agents")
print(response)
```

**Use Multi-Agent System:**
```python
from examples import MultiAgentExample

system = MultiAgentExample()
system.execute_workflow("data_analysis_task")
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Contribution Ideas

- 🐛 Fix bugs or improve existing code
- 📝 Enhance documentation
- 🧪 Add test cases
- 📚 Create example projects
- 🌍 Translate materials

---

## 📄 License

This project is licensed under the **Apache 2.0 License**. See [LICENSE](LICENSE) file for details.

---

## 💬 Support & Community

### Get Help

- 📖 Check [SUMMARY.md](SUMMARY.md) for quick reference
- 🔍 Search existing [GitHub Issues](../../issues)
- 💬 Open a [new issue](../../issues/new) with details
- 📧 Reach out on [GitHub Discussions](../../discussions)

### Show Your Support

⭐ **Star this repository** if you found it helpful!  
It helps others discover the project and motivates continuous improvement.

```
👆 Click the ⭐ button at the top-right of this page
```

### Connect & Share

- 🔗 Share your projects built with this course
- 📢 Tag us in your posts
- 🎓 Tell us about your learning journey

---

## 📊 Repository Stats

![Python](https://img.shields.io/github/languages/top/SujitYalmar/5-Day-AI-Agents-Intensive-Course-?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/SujitYalmar/5-Day-AI-Agents-Intensive-Course-?style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/SujitYalmar/5-Day-AI-Agents-Intensive-Course-?style=flat-square)

---

## 🚀 Quick Navigation

| Resource | Link |
|----------|------|
| **Course Materials** | [Day-1](Day-1_intro_to_agents) → [Day-5](Day-5_evaluation_and_scaling) |
| **Google ADK Docs** | [Official Documentation](https://github.com/googleapis/python-client-libraries) |
| **Gemini API** | [API Reference](https://ai.google.dev/) |
| **Vertex AI** | [Platform Guide](https://cloud.google.com/vertex-ai) |
| **Contributing** | [Guidelines](CONTRIBUTING.md) |

---

<div align="center">

**Made with ❤️ by the AI Agents Community**

*Empowering developers to build intelligent autonomous systems*

</div>
