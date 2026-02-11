"""Core application logic."""


def normalize_text(text: str) -> str:
    """Normalize input text by trimming and collapsing repeated spaces."""
    collapsed = " ".join(text.strip().split())
    return collapsed


def completion_message(project_name: str) -> str:
    """Build a completion-style status message for a project name."""
    normalized = normalize_text(project_name)
    if not normalized:
        return "Your project is complete."
    return f"Project '{normalized}' is complete."
