#!/usr/bin/env python3
"""
Generic Passwords Test File
⚠️ WARNING: All passwords below are FAKE and non-functional.
Used ONLY for research and testing purposes.
"""

# Various password formats commonly found in code
password = "SuperSecretPassword123!"
PASSWORD = "AdminPass2024!"
admin_password = "AdminRoot123"
user_password = "UserPass456!"
db_password = "DBPassword789!"

# Different assignment styles
PASSWORD = 'MySecret@123'
secret = "Secret123!"
SECRET_KEY = "verySecretKey12345"
API_SECRET = "ApiSecret!@#$%"
auth_password = "AuthPass789"

# Hardcoded in function calls
def connect_to_service():
    password = "ServicePassword123"
    secret = "ServiceSecret456"
    return authenticate("admin", "AdminPass123!")

# Dictionary style
credentials = {
    "username": "admin",
    "password": "AdminCredential123!",
    "secret": "CredentialSecret"
}

# Configuration class
class Config:
    PASSWORD = "ConfigPassword123"
    SECRET_KEY = "ConfigSecretKey456"
    DB_PASSWORD = "DatabasePassword789"
    ADMIN_PASSWORD = "AdminPassword000"
