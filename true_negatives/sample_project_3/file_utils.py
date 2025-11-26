#!/usr/bin/env python3
"""
File Utilities Module
This is a clean code example without any secrets.
"""

import os
from pathlib import Path
from typing import List, Optional


def read_file(filepath: str) -> str:
    """Read and return the contents of a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath: str, content: str) -> None:
    """Write content to a file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def append_to_file(filepath: str, content: str) -> None:
    """Append content to a file."""
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(content)


def list_files(directory: str, extension: Optional[str] = None) -> List[str]:
    """List all files in a directory, optionally filtered by extension."""
    path = Path(directory)
    if extension:
        return [str(f) for f in path.glob(f'*{extension}')]
    return [str(f) for f in path.iterdir() if f.is_file()]


def get_file_size(filepath: str) -> int:
    """Get the size of a file in bytes."""
    return os.path.getsize(filepath)


def file_exists(filepath: str) -> bool:
    """Check if a file exists."""
    return os.path.isfile(filepath)


def create_directory(dirpath: str) -> None:
    """Create a directory if it doesn't exist."""
    Path(dirpath).mkdir(parents=True, exist_ok=True)


def count_lines(filepath: str) -> int:
    """Count the number of lines in a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)


class FileHandler:
    """A class for handling file operations."""
    
    def __init__(self, base_dir: str = '.'):
        self.base_dir = Path(base_dir)
    
    def get_path(self, filename: str) -> Path:
        """Get the full path for a filename."""
        return self.base_dir / filename
    
    def read(self, filename: str) -> str:
        """Read a file from the base directory."""
        return read_file(str(self.get_path(filename)))
    
    def write(self, filename: str, content: str) -> None:
        """Write to a file in the base directory."""
        write_file(str(self.get_path(filename)), content)


if __name__ == "__main__":
    handler = FileHandler()
    print(f"Base directory: {handler.base_dir}")
