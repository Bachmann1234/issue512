"""A module with mixed type coverage."""

from typing import Dict, Any
import random


def typed_function(name: str, age: int) -> Dict[str, Any]:
    """A function with type annotations."""
    return {"name": name, "age": age, "id": random.randint(1000, 9999)}


def untyped_function(data):
    """A function without type annotations."""
    if not data:
        return None
    # Added a comment to trigger diff
    
    total = 0
    count = 0  # New untyped variable
    for item in data:
        if hasattr(item, 'value'):
            total += item.value
        else:
            total += int(item)
        count += 1
    return total, count


class MixedClass:
    """A class with some typed and some untyped methods."""
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.items = []
    
    def add_item(self, item):
        """Untyped method."""
        self.items.append(item)
        return len(self.items)
    
    def get_summary(self) -> Dict[str, Any]:
        """Typed method."""
        return {
            "name": self.name,
            "item_count": len(self.items),
            "has_items": bool(self.items)
        }