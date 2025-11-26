#!/usr/bin/env python3
"""
AWS Credentials Test File
⚠️ WARNING: All credentials below are FAKE and non-functional.
Used ONLY for research and testing purposes.
"""

import os

# Example AWS Access Keys (NOT real - follow AWS example format)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Alternative format (also fake)
AWS_ACCESS_KEY = "AKIAI44QH8DHBEXAMPLE"
AWS_SECRET_KEY = "je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY"

# Environment variable style (fake)
aws_access_key_id = "AKIA2GQVWKZ4TESTEXAM"
aws_secret_access_key = "52u7BuqF2rH8j/k9L0mNoPqRsTuVwXyZ1A2B3C4D"

class AWSCredentials:
    """AWS Credentials holder"""
    
    def __init__(self):
        self.access_key = "AKIAIOSFO3DN7EXAMPLE"
        self.secret_key = "wJalrXUtnF5MI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        self.region = "us-east-1"
