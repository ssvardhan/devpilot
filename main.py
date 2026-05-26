# main.py
# ----------------------------------------------------------
# Week 1 smoke test — confirms Claude + Langfuse are working.
# Run with: uv run python main.py
# ----------------------------------------------------------

import os
import anthropic
from langfuse import get_client
from src.devpilot.core.config import (
    ANTHROPIC_API_KEY,
    ANTHROPIC_MODEL,
    LANGFUSE_PUBLIC_KEY,
    LANGFUSE_SECRET_KEY,
    LANGFUSE_BASE_URL,
)

# ── Set up Langfuse env vars before calling get_client() ───
# Langfuse 4.x reads credentials from environment variables.
os.environ["LANGFUSE_PUBLIC_KEY"] = LANGFUSE_PUBLIC_KEY
os.environ["LANGFUSE_SECRET_KEY"] = LANGFUSE_SECRET_KEY
os.environ["LANGFUSE_BASE_URL"]   = LANGFUSE_BASE_URL

# ── Set up clients ─────────────────────────────────────────

claude    = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
langfuse  = get_client()

# ── Make a traced Claude call ──────────────────────────────

def ask_claude(question: str) -> str:
    """
    Send a question to Claude and return the response.
    Uses Langfuse 4.x start_generation() to record the call.
    """

    # Start recording a generation (LLM call) in Langfuse.
    generation = langfuse.start_observation(
    as_type="generation",
    name="ask-claude",
    model=ANTHROPIC_MODEL,
    input=[{"role": "user", "content": question}],
    )

    # Call Claude.
    response = claude.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=1024,
        system="You are a helpful senior data engineer mentor.",
        messages=[
            {"role": "user", "content": question}
        ],
    )

    # Extract the text response.
    answer = response.content[0].text

    # Close the generation with output + token usage.
    generation.update(output=answer)
    generation.end()

    # Flush sends the trace to Langfuse before script exits.
    langfuse.flush()

    return answer


# ── Run it ─────────────────────────────────────────────────

if __name__ == "__main__":
    question = (
        "In one paragraph, what is the most important thing "
        "a data engineer should know about building RAG systems?"
    )

    print("Asking Claude...\n")
    answer = ask_claude(question)

    print("Claude says:")
    print("-" * 60)
    print(answer)
    print("-" * 60)
    print("\n✅ Check your Langfuse dashboard — you should see a trace!")