# Security policy

## Reporting a vulnerability

If you discover a security vulnerability in this project, please report it privately. **Do not open a public GitHub issue.**

- **Preferred**: Use [GitHub Security Advisories](https://github.com/YOUR-ORG/YOUR-REPO/security/advisories/new) (replace `YOUR-ORG/YOUR-REPO` with your repository path) to report the issue. This allows confidential collaboration and coordinated disclosure.
- **Alternative**: Email the maintainers (see the repository or package metadata for contact details) with a description of the vulnerability, steps to reproduce, and any suggested fix. Include your GitHub username if you want to be credited.

We will acknowledge receipt within a reasonable time and will work with you to understand and address the issue. We follow coordinated disclosure: we will not disclose the vulnerability publicly before a fix is available (or before an agreed disclosure date), except where required by law or to meet the 90-day disclosure guideline.

## Supported versions

Security updates are provided for the latest release. We encourage upgrading to the latest version.

## Dependency and supply-chain security

- We use a lockfile (`uv.lock`) and run `pip-audit` (and optionally Dependabot) to track known vulnerabilities in dependencies.
- Before release, run `uv lock --upgrade` and review dependencies; run `uv run pip-audit` to check for known CVEs.
