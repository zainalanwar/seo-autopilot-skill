# SEO-Autopilot Skill

> 🤖 SEO analysis and optimization agent powered by MiMo AI (Xiaomi)

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

SEO-Autopilot is a powerful SEO analysis tool that uses MiMo AI (Xiaomi's Anthropic-compatible API) to detect SEO issues and generate AI-powered fixes for your website.

## ✨ Features

- 🔍 **Full SEO Audit** - Detect issues across multiple pages
- 🤖 **AI-Powered Fixes** - Generate optimized titles, meta descriptions, schema
- 🔗 **WordPress Integration** - Apply fixes directly via REST API
- 💰 **Cost Effective** - Uses MiMo v2.5-pro (~$0.01 per audit)
- 🔒 **Secure** - Environment-based credentials, no hardcoded secrets

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/seo-autopilot-skill.git
cd seo-autopilot-skill
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Credentials

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your credentials
nano .env
```

### 4. Run Setup

```bash
chmod +x setup.sh
./setup.sh
```

### 5. Test Connection

```bash
./seo test
```

## 📖 Usage

### Basic Commands

```bash
# Test MiMo connection
./seo test

# Audit a website
./seo audit https://example.com

# Generate AI-powered fixes
./seo fix https://example.com

# Analyze single page
./seo analyze https://example.com

# Apply fixes to WordPress
./seo apply https://example.com
```

### Save Output to File

```bash
# Save audit report
./seo audit https://example.com --output report.json

# Save fixes
./seo fix https://example.com --output fixes.json
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following:

```bash
# MiMo API Configuration
MIMO_API_KEY=your-mimo-api-key
MIMO_BASE_URL=https://api.xiaomimimo.com/anthropic
MIMO_MODEL=mimo-v2.5-pro

# WordPress Configuration
WP_URL=https://your-site.com
WP_USER=your-username
WP_PASS=your-application-password
```

### Getting MiMo API Key

1. Visit [platform.xiaomimimo.com](https://platform.xiaomimimo.com)
2. Create an account
3. Generate an API key
4. Add to `.env` file

### Getting WordPress Application Password

1. Login to WordPress Admin
2. Go to Users → Your Profile
3. Scroll to "Application Passwords"
4. Create new application password
5. Copy password to `.env` file

## 📁 Project Structure

```
seo-autopilot-skill/
├── README.md           # This file
├── LICENSE             # MIT License
├── requirements.txt    # Python dependencies
├── setup.sh           # Setup wizard
├── seo                # Main CLI script
├── config.py          # Configuration (secure)
├── .env.example       # Environment template
├── .gitignore         # Git ignore rules
└── docs/              # Documentation
    └── USAGE.md       # Detailed usage guide
```

## 🔧 How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    SEO-AUTOPILOT FLOW                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. User runs: ./seo audit https://example.com             │
│                                                             │
│  2. System analyzes:                                        │
│     • Title tags (length, keywords)                         │
│     • Meta descriptions                                     │
│     • Heading structure (H1, H2, H3)                        │
│     • Schema markup                                         │
│     • Security headers                                      │
│                                                             │
│  3. MiMo AI generates:                                      │
│     • Optimized titles                                      │
│     • Compelling meta descriptions                          │
│     • JSON-LD schema                                        │
│                                                             │
│  4. Output:                                                 │
│     • Console report                                        │
│     • JSON file (optional)                                  │
│     • WordPress update (optional)                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Troubleshooting

### "MIMO_API_KEY not set"

```bash
# Load environment variables
source .env

# Or run setup again
./setup.sh
```

### "Connection failed"

1. Check API key is correct
2. Check internet connection
3. Verify MiMo API status

### "WordPress authentication failed"

1. Check WordPress URL
2. Verify username
3. Ensure Application Password is correct

## 📊 Example Output

```
==================================================
SEO-Autopilot Skill v1.0.0
Powered by MiMo v2.5-pro
==================================================

🔍 Running SEO audit for: https://example.com

📊 Audit Results:
  Total Issues: 5
  🔴 High Priority: 1
  🟡 Medium Priority: 2
  🟢 Low Priority: 2

Issues Found:
  1. 🔴 Missing meta description
  2. 🟡 Title too short
  3. 🟡 Missing H1 tag
  4. 🟢 Missing Organization schema
  5. 🟢 Missing security headers
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [MiMo AI](https://platform.xiaomimimo.com) - Xiaomi's AI platform
- [SEO-Autopilot](https://github.com/tentacl-ai/seo-autopilot) - Base SEO tool
- [Anthropic](https://anthropic.com) - API compatibility

## 📞 Support

If you have any questions or issues, please open an issue on GitHub.

---

**Made with ❤️ by OpenCode Agent**
