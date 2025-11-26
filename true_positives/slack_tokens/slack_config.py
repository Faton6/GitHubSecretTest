#!/usr/bin/env python3
"""
Slack Tokens Test File
⚠️ WARNING: All tokens below are FAKE and non-functional.
Used ONLY for research and testing purposes.
"""

# Slack Bot Token (xoxb-)
SLACK_BOT_TOKEN = "xoxb-123456789012-1234567890123-abcdefghijklmnopqrstuvwx"
SLACK_TOKEN = "xoxb-999888777666-5554443332221-AbCdEfGhIjKlMnOpQrStUvWx"

# Slack User Token (xoxp-)
SLACK_USER_TOKEN = "xoxp-123456789012-123456789012-123456789012-abcdefghijklmnopqrstuvwxyz123456"

# Slack App Token (xapp-)
SLACK_APP_TOKEN = "xapp-1-A012345B678-1234567890123-abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

# Slack Webhook URL
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# Legacy Slack Token (xoxa-)
SLACK_LEGACY_TOKEN = "xoxa-2-123456789012-123456789012-123456789012-abcdefghijklmnopqrstuvwx"

class SlackConfig:
    """Slack configuration holder"""
    
    def __init__(self):
        self.bot_token = "xoxb-123456789012-1234567890123-abcdefghijklmnopqrstuvwx"
        self.webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
