#!/usr/bin/env python3
"""
Test Fixtures with Example Credentials
These are INTENTIONALLY fake credentials for testing purposes.
They should NOT trigger secret detection as real leaks.
"""

import pytest

# Example credentials for testing - clearly marked as examples
MOCK_AWS_KEY = "AKIAEXAMPLE12345678"  # Example from AWS documentation
MOCK_AWS_SECRET = "ExampleSecretKeyFromDocumentation12345678"

# Test configuration dictionary
TEST_CONFIG = {
    "api_key": "test_api_key_12345",
    "password": "test_password",
    "secret": "test_secret_value",
    "token": "test_token_value"
}

# Placeholder values for tests
PLACEHOLDER_TOKEN = "<YOUR_TOKEN_HERE>"
PLACEHOLDER_API_KEY = "${API_KEY}"
PLACEHOLDER_PASSWORD = "********"


@pytest.fixture
def mock_credentials():
    """Fixture that returns mock credentials for testing."""
    return {
        "username": "test_user",
        "password": "mock_password_for_testing",
        "api_key": "mock_api_key_for_testing"
    }


@pytest.fixture
def example_config():
    """Example configuration with placeholder values."""
    return {
        "database": {
            "host": "localhost",
            "port": 5432,
            "user": "testuser",
            "password": "testpassword"  # Local test only
        },
        "api": {
            "key": "example_api_key_not_real",
            "secret": "example_secret_not_real"
        }
    }


class TestCredentialHandler:
    """Tests for credential handling - uses mock data."""
    
    def test_mask_password(self):
        """Test that passwords are properly masked."""
        password = "supersecretpassword"
        masked = "*" * len(password)
        assert masked == "*******************"
    
    def test_validate_token_format(self):
        """Test token format validation with example token."""
        example_token = "ghp_ExampleTokenForTestingPurposes1234567"
        assert example_token.startswith("ghp_")
