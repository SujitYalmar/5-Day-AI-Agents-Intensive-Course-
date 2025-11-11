#!/usr/bin/env python3
"""
Simple AI Agent Example using Google's Agent Development Kit (ADK)

This example demonstrates:
- Creating a basic AI agent with Gemini model
- Using Google Search tool for current information
- Running queries through the agent

Based on Kaggle's 5-Day Agents Course - Day 1
Course: https://www.kaggle.com/learn/agents
"""

import os
import asyncio
from google.adk.agents import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search
from google import genai


def setup_environment():
    """
    Setup API key from environment variable.
    For Kaggle: uses Kaggle Secrets
    For local: uses .env file or environment variable
    """
    # Check if running on Kaggle
    try:
        from kaggle_secrets import UserSecretsClient
        api_key = UserSecretsClient().get_secret("GOOGLE_API_KEY")
        os.environ["GOOGLE_API_KEY"] = api_key
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"
        print("✅ Gemini API key loaded from Kaggle Secrets")
    except (ImportError, Exception):
        # Use local environment
        from dotenv import load_dotenv
        load_dotenv()
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("GOOGLE_API_KEY not found. Please set it in .env file or environment.")
        print("✅ Gemini API key loaded from environment")


def create_helpful_agent():
    """
    Create a helpful AI agent with Google Search capability.
    
    Returns:
        Agent: Configured agent instance
    """
    agent = Agent(
        name="helpful_assistant",
        model="gemini-2.5-flash-lite",
        description="A simple agent that can answer general questions.",
        instruction="You are a helpful assistant. Use Google Search for current info or if unsure.",
        tools=[google_search],
    )
    print("\n✅ Agent created successfully!")
    print(f"   Model: {agent.model}")
    print(f"   Tools: {[tool.__name__ if hasattr(tool, '__name__') else str(tool) for tool in agent.tools]}")
    return agent


async def run_agent_query(agent, runner, query: str):
    """
    Run a single query through the agent.
    
    Args:
        agent: The agent instance
        runner: The runner instance
        query: Question to ask the agent
    """
    print(f"\n{'='*70}")
    print(f"💬 Query: {query}")
    print(f"{'-'*70}")
    
    response = await runner.run_debug(query)
    print(f"\n🤖 Agent Response:\n{response}")
    print(f"{'='*70}\n")


async def main():
    """
    Main function demonstrating agent usage with various queries.
    """
    print("\n" + "="*70)
    print("🚀 AI Agent Development with Google ADK")
    print("   Building Intelligent Agents - Day 1 Example")
    print("="*70)
    
    # Setup environment
    setup_environment()
    
    # Create agent
    agent = create_helpful_agent()
    
    # Create runner
    runner = InMemoryRunner(agent=agent)
    print("\n✅ Runner initialized\n")
    
    # Example queries
    queries = [
        "What is Agent Development Kit from Google? What languages is the SDK available in?",
        "What's the weather in London?",
        "Who won the last FIFA World Cup?",
    ]
    
    # Run each query
    for query in queries:
        await run_agent_query(agent, runner, query)
        await asyncio.sleep(1)  # Brief pause between queries


if __name__ == "__main__":
    try:
        # Run the async main function
        asyncio.run(main())
        print("\n✅ Example completed successfully!")
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
