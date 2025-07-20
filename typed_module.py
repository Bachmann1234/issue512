"""A module with proper type annotations."""

from typing import List, Optional


def add_numbers(a: int, b: int) -> int:
    """Add two numbers with proper type hints."""
    return a + b


def process_items(items: List[str]) -> Optional[str]:
    """Process a list of items and return the first one if available."""
    if items:
        return items[0]
    return None


class Calculator:
    """A calculator class with type annotations."""
    
    def __init__(self, initial_value: float = 0.0) -> None:
        self.value: float = initial_value
    
    def multiply(self, factor: float) -> float:
        """Multiply the current value by a factor."""
        self.value *= factor
        return self.value