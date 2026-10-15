# SEO and AI suggestion prototype

An AI-assisted prototype for exploring SEO reporting and text suggestions.
The current `audit` command uses a fixed set of simulated issues: it does not
crawl a website or verify whether those issues exist. Its scores and counts are
illustrations, not measured site performance. Do not use them as client evidence.

## Setup

```bash
git clone https://github.com/zainalanwar/seo-autopilot-skill.git
cd seo-autopilot-skill
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` locally. The CLI reads it directly; there is no `config.py`.
Never publish credentials. Provider pricing and model availability must be checked
with the provider; this project has no verified per-audit cost estimate.

## What the commands actually do

| Command | Current behavior |
| --- | --- |
| `python3 seo test` | Makes a provider API call to test configuration |
| `python3 seo audit URL` | Displays simulated SEO issues and may request AI suggestions |
| `python3 seo analyze URL` | Requests model suggestions using the URL; no page crawl is performed |
| `python3 seo fix URL` | Generates suggested text for predefined issue types |
| `python3 seo apply URL` | Can write a generated title to a matching WordPress page; not a verified SEO repair |

API calls may incur charges. Suggestions use a URL as context, not verified page
content. Review suggestions against the actual page. WordPress application is an
experimental write operation and should only be used on a disposable test site.
It does not implement automatic metadata, schema, or page-content repair.

## Files

- `seo`: CLI, environment loading, provider calls and experimental WordPress integration.
- `report_generator.py`: HTML report rendering.
- `setup.sh`: optional interactive environment configuration.
- `.env.example`: credential names with placeholders.
- `docs/USAGE.md`: usage and limitations.

## Development status

AI-assisted prototype. No production adoption, SEO uplift or complete crawler is
claimed. A useful next step is to replace simulated findings with fetched-page
checks, then test each detector against known HTML fixtures before using results
with clients. Attribution to the original SEO-Autopilot idea remains below.

## Attribution

Inspired by [SEO-Autopilot](https://github.com/tentacl-ai/seo-autopilot).
Uses the provider's Anthropic-compatible interface. Code is MIT licensed.
