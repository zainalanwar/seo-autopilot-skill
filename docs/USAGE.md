# Prototype usage and limits

Start with the setup instructions in [README](../README.md).

```bash
python3 seo audit https://example.com --output demo-report.json
python3 seo audit https://example.com --html --output demo-report.html
```

These commands produce simulated findings. They do not fetch HTML, inspect headers,
measure page speed, or verify SEO problems. With a configured provider they may
make paid API calls to generate suggestions. The model receives a URL rather than
verified page content, so every suggestion needs manual review.

`python3 seo analyze URL` and `python3 seo fix URL` also call the model.
`python3 seo test` checks provider access. None proves a website was audited.

## WordPress experiment

`python3 seo apply URL` looks up a WordPress page and can update its title using
generated text. It does not update page content or SEO-plugin metadata. Use only
on a disposable test site after inspecting the code and keeping a backup.
Do not present this operation as an evidence-based SEO fix.

## Configuration

The script reads `.env` in the current working directory. Use `.env.example` as
a starting point. Keep actual credentials out of source control and screenshots.
The script currently selects its model in code; verify provider access and pricing
before running. No fixed cost-per-audit claim has been validated.
