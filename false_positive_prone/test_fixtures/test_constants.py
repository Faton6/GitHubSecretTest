#!/usr/bin/env python3
"""
Test fixtures with intentionally fake/example credentials.
These should not be flagged as actual secret leaks.
"""

# Example values from official documentation
AWS_EXAMPLE_KEY = "AKIAIOSFODNN7EXAMPLE"  # AWS official example
AWS_EXAMPLE_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # AWS docs

# Regex patterns for testing (not actual secrets)
AWS_KEY_PATTERN = r"AKIA[0-9A-Z]{16}"
AWS_SECRET_PATTERN = r"[A-Za-z0-9/+=]{40}"

# Test data generators
def generate_fake_token():
    """Generate a fake token for testing purposes."""
    import string
    import random
    return "test_" + ''.join(random.choices(string.ascii_letters, k=20))


# Test case data
TEST_CASES = [
    {"input": "password123", "expected": "********"},
    {"input": "api_key_test", "expected": "********"},
    {"input": "secret_value", "expected": "********"},
]

# Commented examples (should not trigger)
# AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
# API_KEY = "your_api_key_here"
# PASSWORD = "change_me_in_production"
