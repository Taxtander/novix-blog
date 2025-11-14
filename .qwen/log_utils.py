import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))
from logger import QwenLogger
import json
import os
from datetime import datetime


def log_current_interaction(content, interaction_type="conversation", metadata=None):
    """
    Log the current interaction to the logs directory
    """
    logger = QwenLogger()
    return logger.log_interaction(interaction_type, content, metadata)


def log_code_modification(file_path, old_content, new_content, description=""):
    """
    Log a code modification with before and after states
    """
    logger = QwenLogger()
    return logger.log_code_change(file_path, old_content, new_content, description)


def log_task_summary(title, content, metadata=None):
    """
    Log a summary of tasks completed
    """
    logger = QwenLogger()
    return logger.log_summary(title, content, metadata)


def save_conversation_state(conversation_data, task_status=None):
    """
    Save the current state of the conversation
    """
    logger = QwenLogger()
    return logger.save_state(conversation_data, task_status)


def create_log_entry(entry_type, data):
    """
    Create a general log entry of specified type with provided data
    """
    logger = QwenLogger()
    
    if entry_type == "interaction":
        return logger.log_interaction(
            data.get("interaction_type", "general"),
            data.get("content", ""),
            data.get("metadata", {})
        )
    elif entry_type == "code_change":
        return logger.log_code_change(
            data.get("file_path", ""),
            data.get("old_content", ""),
            data.get("new_content", ""),
            data.get("change_description", "")
        )
    elif entry_type == "summary":
        return logger.log_summary(
            data.get("title", "Summary"),
            data.get("summary_content", ""),
            data.get("metadata", {})
        )
    elif entry_type == "state":
        return logger.save_state(
            data.get("conversation_state", {}),
            data.get("task_status", {})
        )
    else:
        raise ValueError(f"Unknown log entry type: {entry_type}")


# Example usage functions
def example_usage():
    """
    Demonstrates how to use the logging utilities
    """
    # Log an interaction
    log_current_interaction(
        "User requested to update the login form validation",
        "command",
        {"user_request": True, "priority": "high"}
    )
    
    # Log a code change
    log_code_modification(
        "app/forms.py",
        "def validate_email(email):\n    return '@' in email",
        "def validate_email(email):\n    import re\n    pattern = r'^[\\w\\.-]+@[^\\w\\.-]+\\.[a-zA-Z]{2,}$'\n    return re.match(pattern, email) is not None",
        "Enhanced email validation with regex pattern"
    )
    
    # Log a task summary
    log_task_summary(
        "Login Form Validation Update",
        "Updated the email validation in the login form to use a more robust regex pattern. "
        "Also added validation for password strength requirements.",
        {"status": "completed", "date": str(datetime.now())}
    )


if __name__ == "__main__":
    example_usage()
    print("Example usage completed. Check the .qwen directory for generated logs.")