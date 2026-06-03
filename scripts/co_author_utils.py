"""Shared utilities for adding agent co-author attribution to GitHub interactions.

This module provides standardized formatting for agent identity across:
- Git commit messages (Co-authored-by trailers)
- PR bodies (Co-authored-by trailers)
- PR comments (Uniform markdown headers)

Usage:
    from co_author_utils import co_author_trailer, format_agent_header

    # For commit messages / PR bodies
    trailer = co_author_trailer("Aider Coder", tier="tier1", model="openrouter/deepseek/deepseek-v4-flash")
    commit_msg = f"fix: resolve bug\\n\\n{trailer}"

    # For PR comments
    header = format_agent_header("aider-reviewer", "openrouter/anthropic/claude-3-opus", "tier2", "code-review")
"""

from __future__ import annotations


def co_author_trailer(agent: str, tier: str = "", model: str = "") -> str:
    """
    Generate a Co-authored-by trailer string for git commits and PR bodies.

    Args:
        agent: The agent name (e.g., "Aider Coder", "Issue Resolver")
        tier: Optional tier/profile (e.g., "tier1", "tier2")
        model: Optional model identifier (e.g., "openrouter/deepseek/deepseek-v4-flash")

    Returns:
        Formatted trailer string, or empty string if agent is empty.

    Example:
        >>> co_author_trailer("Aider Coder", tier="tier1", model="deepseek-v4-flash")
        'Co-authored-by: Aider Coder (tier1) <deepseek-v4-flash>'
    """
    if not agent:
        return ""

    trailer = f"Co-authored-by: {agent}"
    if tier:
        trailer += f" ({tier})"
    if model:
        trailer += f" <{model}>"

    return trailer


def format_agent_header(agent: str, model: str, tier: str, task: str) -> str:
    """
    Format a uniform markdown header for PR comments showing agent identity and task.

    Args:
        agent: The agent name (e.g., "aider-coder", "aider-reviewer")
        model: The model identifier
        tier: The review/coding tier (e.g., "tier1", "tier2")
        task: The specific task being performed (e.g., "code-generation (attempt 1/3)")

    Returns:
        Formatted markdown header string.

    Example:
        >>> format_agent_header("aider-coder", "deepseek-v4-flash", "tier1", "code-generation")
        '**Agent:** aider-coder | **Model:** deepseek-v4-flash | **Tier:** tier1 | **Task:** code-generation'
    """
    parts = [f"**Agent:** {agent}"]
    if model:
        parts.append(f"**Model:** {model}")
    if tier:
        parts.append(f"**Tier:** {tier}")
    if task:
        parts.append(f"**Task:** {task}")

    return " | ".join(parts)


if __name__ == "__main__":
    # Quick self-test
    print("Testing co_author_trailer():")
    print(f"  {co_author_trailer('Aider Coder', tier='tier1', model='deepseek-v4-flash')}")
    print(f"  {co_author_trailer('Issue Resolver', model='qwen3-35b-uncensored')}")
    print(f"  {co_author_trailer('Release Manager')}")
    print()
    print("Testing format_agent_header():")
    print(f"  {format_agent_header('aider-coder', 'deepseek-v4-flash', 'tier1', 'code-generation (attempt 1/3)')}")
    print(f"  {format_agent_header('aider-reviewer', 'claude-3-opus', 'tier2', 'adversarial-review')}")
