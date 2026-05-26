# src/devpilot/core/config.py
# ----------------------------------------------------------
# Loads environment variables from .env and exposes them
# as a typed config object the rest of the app can import.
# ----------------------------------------------------------

import os
from dotenv import load_dotenv

# Load the .env file into environment variables.
# This must run before anything tries to read os.getenv().
load_dotenv()


def get_required(key: str) -> str:
    """
    Get an environment variable or raise a clear error if missing.
    Better than silent None values that cause confusing errors later.
    """
    value = os.getenv(key)
    if not value:
        raise ValueError(
            f"Missing required environment variable: {key}\n"
            f"Make sure it's set in your .env file."
        )
    return value


# ── Anthropic ──────────────────────────────────────────────
ANTHROPIC_API_KEY = get_required("ANTHROPIC_API_KEY")
ANTHROPIC_MODEL = "claude-sonnet-4-5"

# ── Langfuse ───────────────────────────────────────────────
LANGFUSE_PUBLIC_KEY = get_required("LANGFUSE_PUBLIC_KEY")
LANGFUSE_SECRET_KEY = get_required("LANGFUSE_SECRET_KEY")
LANGFUSE_BASE_URL = get_required("LANGFUSE_BASE_URL")