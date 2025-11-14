import json
import os
from datetime import datetime
from pathlib import Path


class QwenLogger:
    """
    A logging system for Qwen interactions, code changes, and summaries.
    Stores logs in JSON format in the .qwen directory.
    """
    
    def __init__(self, base_dir="G:/Projects/web/novix-blog/.qwen"):
        self.base_dir = Path(base_dir)
        self.logs_dir = self.base_dir / "logs"
        self.code_changes_dir = self.base_dir / "code_changes"
        self.summaries_dir = self.base_dir / "summaries"
        
        # Create directories if they don't exist
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        self.code_changes_dir.mkdir(parents=True, exist_ok=True)
        self.summaries_dir.mkdir(parents=True, exist_ok=True)
    
    def log_interaction(self, interaction_type, content, metadata=None):
        """
        Log an interaction (conversation, command, etc.)
        
        Args:
            interaction_type (str): Type of interaction (e.g., 'conversation', 'command')
            content (str): The content of the interaction
            metadata (dict): Additional metadata about the interaction
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"interaction_{timestamp}.json"
        
        log_entry = {
            "timestamp": timestamp,
            "interaction_type": interaction_type,
            "content": content,
            "metadata": metadata or {}
        }
        
        file_path = self.logs_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(log_entry, f, indent=2, ensure_ascii=False)
        
        return str(file_path)
    
    def log_code_change(self, file_path, old_content, new_content, change_description=""):
        """
        Log a code change with original and new content
        
        Args:
            file_path (str): Path of the file being changed
            old_content (str): Original content of the file
            new_content (str): New content of the file
            change_description (str): Description of the change made
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"code_change_{timestamp}.json"
        
        log_entry = {
            "timestamp": timestamp,
            "file_path": file_path,
            "old_content": old_content,
            "new_content": new_content,
            "change_description": change_description
        }
        
        file_path = self.code_changes_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(log_entry, f, indent=2, ensure_ascii=False)
        
        return str(file_path)
    
    def log_summary(self, title, summary_content, metadata=None):
        """
        Log a summary of work done
        
        Args:
            title (str): Title of the summary
            summary_content (str): Content of the summary
            metadata (dict): Additional metadata about the summary
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"summary_{timestamp}.json"
        
        log_entry = {
            "timestamp": timestamp,
            "title": title,
            "summary_content": summary_content,
            "metadata": metadata or {}
        }
        
        file_path = self.summaries_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(log_entry, f, indent=2, ensure_ascii=False)
        
        return str(file_path)
    
    def save_state(self, conversation_state, task_status=None):
        """
        Save the current state of the conversation and tasks
        
        Args:
            conversation_state (dict): Current state of the conversation
            task_status (dict): Current status of tasks (optional)
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"state_{timestamp}.json"
        
        state_entry = {
            "timestamp": timestamp,
            "conversation_state": conversation_state,
            "task_status": task_status or {}
        }
        
        file_path = self.logs_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(state_entry, f, indent=2, ensure_ascii=False)
        
        return str(file_path)


# Example usage
if __name__ == "__main__":
    logger = QwenLogger()
    
    # Example of logging an interaction
    logger.log_interaction(
        "conversation",
        "User asked about the weather",
        {"user": "example_user", "topic": "weather"}
    )
    
    # Example of logging a code change
    logger.log_code_change(
        "example.py",
        "def hello():\n    print('Hello')",
        "def hello():\n    print('Hello, World!')",
        "Updated print statement"
    )
    
    # Example of logging a summary
    logger.log_summary(
        "Daily Work Summary",
        "Completed the weather API integration and fixed the authentication bug.",
        {"date": "2023-06-15", "status": "completed"}
    )
    
    print("Logging system test completed. Check the .qwen directory for log files.")