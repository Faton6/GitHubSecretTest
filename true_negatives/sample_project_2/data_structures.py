#!/usr/bin/env python3
"""
Data Structures Implementation
This is a clean code example without any secrets.
"""

from typing import Any, Optional, List


class Node:
    """A node in a linked list."""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None


class LinkedList:
    """A singly linked list implementation."""
    
    def __init__(self):
        self.head: Optional[Node] = None
        self._size = 0
    
    def append(self, data: Any) -> None:
        """Add an element to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
    
    def prepend(self, data: Any) -> None:
        """Add an element to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def remove(self, data: Any) -> bool:
        """Remove the first occurrence of data."""
        if not self.head:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False
    
    def to_list(self) -> List[Any]:
        """Convert the linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __len__(self) -> int:
        return self._size


class Stack:
    """A stack implementation using a list."""
    
    def __init__(self):
        self._items: List[Any] = []
    
    def push(self, item: Any) -> None:
        """Push an item onto the stack."""
        self._items.append(item)
    
    def pop(self) -> Any:
        """Pop and return the top item."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()
    
    def peek(self) -> Any:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll.to_list())
