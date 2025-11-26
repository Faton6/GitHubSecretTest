#!/usr/bin/env python3
"""
Sample Calculator Application
This is a clean code example without any secrets.
"""

import math
from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Add two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """Calculate base raised to the power of exponent."""
    return math.pow(base, exponent)


def square_root(n: Number) -> float:
    """Calculate the square root of n."""
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(n)


class Calculator:
    """A simple calculator class."""
    
    def __init__(self):
        self.history = []
    
    def calculate(self, operation: str, a: Number, b: Number = None) -> Number:
        """Perform a calculation and store in history."""
        operations = {
            'add': lambda: add(a, b),
            'subtract': lambda: subtract(a, b),
            'multiply': lambda: multiply(a, b),
            'divide': lambda: divide(a, b),
            'power': lambda: power(a, b),
            'sqrt': lambda: square_root(a),
        }
        
        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")
        
        result = operations[operation]()
        self.history.append({
            'operation': operation,
            'a': a,
            'b': b,
            'result': result
        })
        return result


if __name__ == "__main__":
    calc = Calculator()
    print(calc.calculate('add', 5, 3))
    print(calc.calculate('multiply', 4, 7))
