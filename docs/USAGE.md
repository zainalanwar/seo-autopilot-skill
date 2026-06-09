# SEO-Autopilot Usage Guide

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Basic Usage](#basic-usage)
- [Advanced Usage](#advanced-usage)
- [WordPress Integration](#wordpress-integration)
- [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- MiMo API key
- WordPress site with REST API enabled

### Install Steps

```bash
# 1. Clone repository
git clone https://github.com/yourusername/seo-autopilot-skill.git
cd seo-autopilot-skill

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run setup
./setup.sh
```

## Configuration

### Environment Variables

Create a `.env` file with:

```bash
# MiMo API
MIMO_API_KEY=your-api-key
MIMO_BASE_URL=https://api.xiaomimimo.com/anthropic
MIMO_MODEL=mimo-v2.5-pro

# WordPress
WP_URL=https://your-site.com
WP_USER=your-username
WP_PASS=your-application-password
```

### Getting Credentials

#### MiMo API Key

1. Visit https://platform.xiaomimimo.com
2. Create account or login
3. Navigate to API Keys
4. Generate new key
5. Copy to `.env`

#### WordPress Application Password

1. Login to WordPress Admin
2. Go to Users → Your Profile
3. Scroll to "Application Passwords"
4. Enter name (e.g., "SEO-Autopilot")
5. Click "Add New Application Password"
6. Copy the generated password

## Basic Usage

### Test Connection

```bash
./seo test
```

Expected output:
```
✓ MiMo API connected successfully
  Base URL: https://api.xiaomimimo.com/anthropic/
  Model: mimo-v2.5-pro
```

### Run SEO Audit

```bash
./seo audit https://example.com
```

Output includes:
- Total issues found
- Issues by priority (high/medium/low)
- List of specific issues

### Generate Fixes

```bash
./seo fix https://example.com
```

Output includes:
- AI-generated title suggestions
- Meta description recommendations
- Schema markup suggestions

### Analyze Single Page

```bash
./seo analyze https://example.com
```

Provides detailed analysis of:
- Title tag
- Meta description
- Heading structure
- Schema markup

## Advanced Usage

### Save Output to File

```bash
# Save audit report
./seo audit https://example.com --output audit-report.json

# Save fixes
./seo fix https://example.com --output seo-fixes.json
```

### Fix Specific Issue Type

```bash
# Fix only missing meta descriptions
./seo fix https://example.com --type missing_meta_description

# Fix only short titles
./seo fix https://example.com --type short_title
```

### Apply Fixes to WordPress

```bash
./seo apply https://example.com
```

This will:
1. Generate fixes using MiMo
2. Find the page in WordPress
3. Update the title/content

## WordPress Integration

### How It Works

SEO-Autopilot uses WordPress REST API to:
- Read page data
- Update page titles
- Update page content
- Manage page metadata

### REST API Endpoints Used

```
GET  /wp-json/wp/v2/pages           # List pages
GET  /wp-json/wp/v2/pages/{id}      # Get page
POST /wp-json/wp/v2/pages/{id}      # Update page
```

### Authentication

Uses HTTP Basic Auth with Application Password:
```
Authorization: Basic base64(username:password)
```

## Troubleshooting

### Issue: "MIMO_API_KEY not set"

**Solution:**
```bash
# Option 1: Load environment
source .env

# Option 2: Run setup
./setup.sh

# Option 3: Set manually
export MIMO_API_KEY="your-key"
```

### Issue: "Connection failed"

**Check:**
1. API key is correct
2. Internet connection works
3. MiMo API is accessible

**Test:**
```bash
curl -X POST https://api.xiaomimimo.com/anthropic/v1/messages \
  -H "api-key: YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"mimo-v2.5-pro","max_tokens":50,"messages":[{"role":"user","content":"test"}]}'
```

### Issue: "WordPress authentication failed"

**Check:**
1. WordPress URL is correct
2. Username is correct
3. Application Password is correct
4. REST API is enabled

**Test:**
```bash
curl -u "username:application-password" https://your-site.com/wp-json/wp/v2/users/me
```

### Issue: "Page not found"

**Check:**
1. Page slug exists
2. Page is published
3. User has permission to read

## API Reference

### MiMo API

- **Endpoint:** https://api.xiaomimimo.com/anthropic/v1/messages
- **Auth:** `api-key` header
- **Model:** mimo-v2.5-pro
- **Format:** Anthropic Messages API

### WordPress REST API

- **Endpoint:** https://your-site.com/wp-json/wp/v2/
- **Auth:** HTTP Basic Auth
- **Documentation:** https://developer.wordpress.org/rest-api/

## Support

For issues or questions:
1. Check this documentation
2. Search existing GitHub issues
3. Create new issue with details
