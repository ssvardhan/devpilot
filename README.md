# DevPilot

An agentic developer assistant platform — multi-agent system 
for developer workflows using LangGraph, RAG, and Claude.

## Status

- [x] Week 1: Foundation — Claude API + Langfuse tracing ✅
- [ ] Week 2: Docs agent + RAG pipeline
- [ ] Week 3: Multi-agent orchestration with LangGraph
- [ ] Week 4: Tool-using agents
- [ ] Week 5: Evaluations + observability
- [ ] Week 6: Production deployment

## Stack

Python 3.12 · FastAPI · LangGraph · Anthropic Claude · 
ChromaDB · Langfuse · Docker · GitHub Actions

## Architecture

Multi-agent system with a LangGraph supervisor routing 
questions to specialised agents:
- Docs Agent (RAG over internal knowledge base)
- Catalog Agent (service registry queries)
- Scaffolding Agent (code generation)
- Code Review Agent (diff analysis)

## Setup

1. Clone the repo
2. Copy `.env.example` to `.env` and fill in your keys
3. Run `uv sync` to install dependencies
4. Run `uv run python main.py` to test the setup