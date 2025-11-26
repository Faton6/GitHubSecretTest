# Configuration Guide

## Setting Up API Keys

To configure your API keys, follow these steps:

### AWS Configuration

1. Get your AWS credentials from the AWS Console
2. Set them as environment variables:

```bash
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

**Note:** The values above are examples from AWS documentation. Replace them with your actual credentials.

### GitHub Token Setup

Create a Personal Access Token in GitHub Settings:

```bash
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Database Configuration

Example connection string format:

```
postgresql://username:password@hostname:5432/database
```

For local development:
```
postgresql://dev_user:dev_password@localhost:5432/myapp_dev
```

## Security Best Practices

- Never commit real credentials to version control
- Use environment variables for sensitive data
- Rotate secrets regularly
- Use secret management tools in production

## Example Configuration File

```json
{
  "api_key": "YOUR_API_KEY_HERE",
  "password": "YOUR_PASSWORD_HERE",
  "secret": "YOUR_SECRET_HERE"
}
```

Replace the placeholder values with your actual credentials.
