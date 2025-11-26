#!/usr/bin/env python3
"""
GitHub Tokens Test File
⚠️ WARNING: All tokens below are FAKE and non-functional.
Used ONLY for research and testing purposes.
"""

# GitHub Personal Access Tokens (NEW format - ghp_)
GITHUB_TOKEN = "ghp_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890"
GITHUB_PAT = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GH_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"

# GitHub OAuth Tokens (gho_)
GITHUB_OAUTH_TOKEN = "gho_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GH_OAUTH = "gho_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890"

# GitHub App Tokens (ghs_)
GITHUB_APP_TOKEN = "ghs_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# GitHub Refresh Tokens (ghr_)
GITHUB_REFRESH_TOKEN = "ghr_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Old format GitHub tokens (40 chars hex)
GITHUB_TOKEN_OLD = "ghp_0123456789abcdef0123456789abcdef01234567"

class GitHubAuth:
    """GitHub Authentication handler"""
    
    def __init__(self):
        self.token = "ghp_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890"
        self.oauth_token = "gho_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
