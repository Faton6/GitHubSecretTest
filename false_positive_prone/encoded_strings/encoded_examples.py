#!/usr/bin/env python3
"""
Examples of Base64 and Hex encoded strings that are NOT secrets.
These should not trigger false positives in secret detection.
"""

import base64
import hashlib

# Base64 encoded regular text (NOT secrets)
HELLO_WORLD_B64 = "SGVsbG8gV29ybGQh"  # "Hello World!" in base64
LOREM_IPSUM_B64 = "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQ="  # Lorem ipsum...

# Hex encoded strings (NOT secrets)
HELLO_HEX = "48656c6c6f20576f726c6421"  # "Hello World!" in hex
COLOR_HEX = "#FF5733"  # Color code
MAC_ADDRESS = "00:1A:2B:3C:4D:5E"

# UUID (not a secret)
USER_UUID = "550e8400-e29b-41d4-a716-446655440000"
SESSION_UUID = "6ba7b810-9dad-11d1-80b4-00c04fd430c8"

# Hash values (not secrets - these are outputs, not inputs)
FILE_MD5 = "d41d8cd98f00b204e9800998ecf8427e"
FILE_SHA256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
FILE_SHA1 = "da39a3ee5e6b4b0d3255bfef95601890afd80709"

# Encrypted placeholder (not the actual key)
ENCRYPTED_DATA = "U2FsdGVkX1+vupppZksvRf5pq5g5XjFRIipRkwB0K1Y="

# Sample JWT structure (with fake payload - for documentation)
EXAMPLE_JWT_STRUCTURE = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

# Public key (not a secret - public keys are meant to be shared)
RSA_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0Z3VS5JJcds3xfn/ygWy
F8PbnGy0AHB7MmVo4WmhvZjQ8g+WzC8cPxJT4FC+E7SnbzGkCv8wFpWjRfmZrK5i
-----END PUBLIC KEY-----"""


def decode_examples():
    """Demonstrate that these are just encoded text, not secrets."""
    print(f"Hello World B64: {base64.b64decode(HELLO_WORLD_B64).decode()}")
    print(f"Hello Hex: {bytes.fromhex(HELLO_HEX).decode()}")


# Random-looking strings that aren't secrets
CORRELATION_ID = "f47ac10b-58cc-4372-a567-0e02b2c3d479"
TRACKING_ID = "UA-12345678-1"  # Google Analytics format
BUILD_NUMBER = "20231126-abcd1234"
VERSION_HASH = "a1b2c3d4e5f6"
