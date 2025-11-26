#!/usr/bin/env python3
"""
HTTP Client Module
This is a clean code example without any secrets.
Uses environment variables for configuration.
"""

import os
from typing import Dict, Any, Optional
from urllib.parse import urljoin


class HTTPClient:
    """A simple HTTP client wrapper."""
    
    def __init__(self, base_url: Optional[str] = None):
        # Get base URL from environment variable, not hardcoded
        self.base_url = base_url or os.environ.get('API_BASE_URL', 'http://localhost:8000')
        self.timeout = int(os.environ.get('HTTP_TIMEOUT', '30'))
        self.headers: Dict[str, str] = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def set_auth_header(self, token: str) -> None:
        """Set authorization header from provided token."""
        # Token is passed in, not hardcoded
        self.headers['Authorization'] = f'Bearer {token}'
    
    def build_url(self, endpoint: str) -> str:
        """Build full URL from base URL and endpoint."""
        return urljoin(self.base_url, endpoint)
    
    def get_config(self) -> Dict[str, Any]:
        """Get current client configuration."""
        return {
            'base_url': self.base_url,
            'timeout': self.timeout,
            'headers': {k: v for k, v in self.headers.items() 
                       if k != 'Authorization'}
        }


def get_api_client() -> HTTPClient:
    """Factory function to create an API client."""
    client = HTTPClient()
    
    # Get token from environment variable
    token = os.environ.get('API_TOKEN')
    if token:
        client.set_auth_header(token)
    
    return client


if __name__ == "__main__":
    client = get_api_client()
    print(client.get_config())
