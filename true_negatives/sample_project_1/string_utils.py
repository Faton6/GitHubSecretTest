#!/usr/bin/env python3
"""
String Utilities Module
This is a clean code example without any secrets.
"""

from typing import List, Optional


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def count_words(s: str) -> int:
    """Count the number of words in a string."""
    return len(s.split())


def find_longest_word(s: str) -> str:
    """Find the longest word in a string."""
    words = s.split()
    if not words:
        return ""
    return max(words, key=len)


def capitalize_words(s: str) -> str:
    """Capitalize the first letter of each word."""
    return ' '.join(word.capitalize() for word in s.split())


def remove_duplicates(s: str) -> str:
    """Remove duplicate characters while preserving order."""
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


class StringProcessor:
    """A class for processing strings."""
    
    def __init__(self, text: str):
        self.text = text
        self.word_count = count_words(text)
    
    def get_statistics(self) -> dict:
        """Get statistics about the text."""
        return {
            'length': len(self.text),
            'word_count': self.word_count,
            'char_count': len(self.text.replace(' ', '')),
            'is_palindrome': is_palindrome(self.text),
            'longest_word': find_longest_word(self.text)
        }


if __name__ == "__main__":
    processor = StringProcessor("Hello World Python Programming")
    print(processor.get_statistics())
