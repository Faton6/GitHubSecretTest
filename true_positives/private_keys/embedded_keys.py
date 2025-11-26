#!/usr/bin/env python3
"""
Private Keys embedded in code
⚠️ WARNING: All keys below are FAKE and non-functional.
Used ONLY for research and testing purposes.
"""

# RSA Private Key embedded in code (common security mistake)
RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF8PbnGy0AHB7MmVo4WmhvZjQ8g+W
zC8cPxJT4FC+E7SnbzGkCv8wFpWjRfmZrK5iyX3kCpFSxwZTSUwBiQsS9RwZ0PXT
ABCDEFGHIJKLMNOP0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL
MNOP0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP01234567
-----END RSA PRIVATE KEY-----"""

# DSA Private Key
DSA_PRIVATE_KEY = """-----BEGIN DSA PRIVATE KEY-----
MIIBugIBAAKBgQDEKORRvqfPK/hGo5ZE5+LZZqhmJxhN0/3P2Qn1zJ8G0XHx0X3g
ABCDEFGHIJKLMNOP0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL
MNOP0123456789abcdefghijklmnopqrstuvwxyz==
-----END DSA PRIVATE KEY-----"""

# SSH Private Key
SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBxTj/0Y1Y0Z3k5T1+ABCDEFGHIJKLMNOP0123456789abcdAAAAJgAAAB
-----END OPENSSH PRIVATE KEY-----"""

def get_ssh_key():
    """Return the SSH private key - INSECURE PRACTICE"""
    return SSH_PRIVATE_KEY
