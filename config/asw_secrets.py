#!/usr/bin/env python3
"""
AWS Secrets Test File
⚠️ WARNING: All credentials below are FAKE and non-functional.
Used ONLY for research and testing purposes.
"""

import os
from typing import Dict, Optional

class AWSConfig:
    """Simulated AWS configuration with example credentials"""
    
    # Example AWS Access Keys (NOT real)
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    # Alternative formats
    AWS_KEY_ALTERNATE = "AKIAI44QH8DHBEXAMPLE"
    AWS_SECRET_ALTERNATE = "je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY"
    
    # From environment (this would trigger secret scanning)
    AWS_ACCESS_KEY_FROM_ENV = os.getenv(
        "AWS_ACCESS_KEY",
        "AKIA2GQVWKZ4TESTEXAMPLE"
    )
    
    def __init__(self, profile: str = "default"):
        self.profile = profile
        self._credentials = self._load_credentials()
    
    def _load_credentials(self) -> Dict[str, str]:
        """Load AWS credentials from config"""
        return {
            "access_key": self.AWS_ACCESS_KEY_ID,
            "secret_key": self.AWS_SECRET_ACCESS_KEY,
            "region": "us-east-1"
        }
    
    def get_client(self, service: str):
        """Example of how client would be initialized"""
        # In real code, this would use boto3
        return {
            "service": service,
            "credentials": self._credentials
        }


# Credentials hardcoded in dictionaries (common mistake)
AWS_PROFILES = {
    "production": {
        "access_key_id": "AKIA3HFQU2LKEXAMPLE1",
        "secret_access_key": "52u7BuqF2rH8j/k9L0mNoPqRsTuVwXyZ1A2B3EXAMPLE",
        "region": "eu-west-1",
        "mfa_serial": "arn:aws:iam::123456789012:mfa/user"
    },
    "staging": {
     
