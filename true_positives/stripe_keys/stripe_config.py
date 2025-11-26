#!/usr/bin/env python3
"""
Stripe API Keys Test File
⚠️ WARNING: All keys below are FAKE and non-functional.
Used ONLY for research and testing purposes.
"""

# Stripe Secret Keys (Live mode - sk_live_)
STRIPE_SECRET_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc123456789abcdefghijklmnopqrstuvwxyz"
STRIPE_LIVE_KEY = "sk_live_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Stripe Secret Keys (Test mode - sk_test_)
STRIPE_TEST_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc123456789abcdefghijklmnopqrstuvwxyz"

# Stripe Publishable Keys (pk_live_, pk_test_)
STRIPE_PUBLISHABLE_KEY = "pk_live_4eC39HqLyjWDarjtT1zdp7dc123456789abcdefghijklmnopqrstuvwxyz"
STRIPE_TEST_PUBLISHABLE_KEY = "pk_test_4eC39HqLyjWDarjtT1zdp7dc123456789abcdefghijklmnopqrstuvwxyz"

# Stripe Restricted Key (rk_live_)
STRIPE_RESTRICTED_KEY = "rk_live_4eC39HqLyjWDarjtT1zdp7dc123456789abcdefghijklmnopqrstuvwxyz"

# Stripe Webhook Secret
STRIPE_WEBHOOK_SECRET = "whsec_1234567890abcdefghijklmnopqrstuvwxyz"

class StripeConfig:
    """Stripe configuration holder"""
    
    def __init__(self):
        self.secret_key = "sk_live_4eC39HqLyjWDarjtT1zdp7dc123456789abcdefghijklmnopqrstuvwxyz"
        self.publishable_key = "pk_live_4eC39HqLyjWDarjtT1zdp7dc123456789abcdefghijklmnopqrstuvwxyz"
        self.webhook_secret = "whsec_1234567890abcdefghijklmnopqrstuvwxyz"
