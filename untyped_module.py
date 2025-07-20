"""A module with no type annotations."""

import json
import os


def load_config(filename):
    """Load configuration from a file."""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}


def process_data(data):
    """Process some data without type hints."""
    result = []
    for item in data:
        if isinstance(item, str):
            result.append(item.upper())
        elif isinstance(item, int):
            result.append(item * 2)
    return result


class DataProcessor:
    """A data processor without type annotations."""
    
    def __init__(self, config=None):
        self.config = config or {}
        self.processed_count = 0
    
    def process_batch(self, items):
        """Process a batch of items."""
        processed = []
        for item in items:
            processed.append(self._transform_item(item))
            self.processed_count += 1
        return processed
    
    def _transform_item(self, item):
        """Transform a single item."""
        return str(item).strip().lower()