# Qwen Logging System

This directory contains a logging system for tracking interactions, code changes, and summaries during development with Qwen.

## Directory Structure

- `logs/` - Stores general interaction logs and state snapshots
- `code_changes/` - Stores logs of all code modifications with before/after content
- `summaries/` - Stores task summaries and work summaries
- `logger.py` - Main logging class and functionality
- `log_utils.py` - Utility functions for common logging tasks
- `logger_config.json` - Configuration for the logging system

## Usage

### Direct Logging
You can use the `QwenLogger` class directly:

```python
from .qwen.logger import QwenLogger

logger = QwenLogger()
logger.log_interaction("conversation", "Conversation content here")
logger.log_code_change("file_path", "old_content", "new_content", "change description")
logger.log_summary("Summary title", "Summary content")
```

### Using Utility Functions
The `log_utils.py` file provides convenient functions:

```python
from .qwen.log_utils import log_current_interaction, log_code_modification, log_task_summary

log_current_interaction("Content of interaction", "interaction_type", metadata)
log_code_modification("file_path", "old_content", "new_content", "description")
log_task_summary("Title", "Summary content", metadata)
```

## Log Entry Format

All logs are stored in JSON format with the following structure:

### Interaction Logs
```json
{
  "timestamp": "YYYY-MM-DD_HH-MM-SS",
  "interaction_type": "conversation|command|etc",
  "content": "The actual content",
  "metadata": {}
}
```

### Code Change Logs
```json
{
  "timestamp": "YYYY-MM-DD_HH-MM-SS",
  "file_path": "path/to/file",
  "old_content": "original content",
  "new_content": "modified content",
  "change_description": "Description of the change"
}
```

### Summary Logs
```json
{
  "timestamp": "YYYY-MM-DD_HH-MM-SS",
  "title": "Summary title",
  "summary_content": "Detailed summary",
  "metadata": {}
}
```

## Configuration

The `logger_config.json` file allows you to customize:
- Log directory path
- Log retention period
- Maximum file sizes