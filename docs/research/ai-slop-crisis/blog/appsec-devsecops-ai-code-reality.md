# What AppSec Teams Are Actually Seeing in AI-Generated Code (and What to Do About It)

*Your scan results are telling you something. Here is the data that confirms it -- and the inline governance patterns that actually work.*

---

## The Numbers You Suspected Are Real

If you run an AppSec or DevSecOps program, you have probably noticed your SAST findings ticking up over the past 12-18 months without a proportional increase in headcount or feature velocity. You are not imagining it. Six independent studies now confirm what your scan results already suggest: AI-generated code carries a measurably higher vulnerability density than human-written code, and the problem is not improving with newer models.

**AppSec Santa (2026)** tested 534 AI-generated code samples across six LLMs -- GPT-5.2, Claude Opus 4.6, Gemini 2.5 Pro, DeepSeek V3, Llama 4 Maverick, and Grok 4 -- against the OWASP Top 10. **25.1% of samples contained a confirmed security vulnerability.** One in four. SSRF led with 32 findings; injection flaws accounted for 33.1% of all confirmed vulnerabilities.

**Veracode (2025)** tested more than 100 LLMs across 4 languages and found AI-generated code contains **2.74x more vulnerabilities** than human-written code. The failure rate on secure coding benchmarks: 45%.

**Apiiro** analyzed Fortune 50 enterprise codebases between December 2024 and June 2025. The findings are specific: **322% more privilege escalation paths**, **153% more design flaws**, and **Azure credentials exposed nearly twice as often** in AI-generated code versus human-written baselines. By June 2025, AI-generated code was adding over 10,000 new security findings per month across their sample -- a 10x increase from six months prior.

**CodeRabbit** found AI-generated code was **1.88x more likely to introduce vulnerabilities** and that production incidents per pull request increased **23.5%** between December 2025 and early 2026.

These are not hypothetical benchmark numbers. They are measured against real codebases, real PRs, and real production environments.

## The Security Pass Rate Has Not Moved in Two Years

This is the finding that should concern you most.

Veracode's Spring 2026 update tested the latest models from every major vendor. Despite AI coding assistants now achieving syntax correctness rates exceeding 95%, **security pass rates remain stuck at approximately 55%** -- virtually identical to where they stood two years ago. Nearly half of all AI-generated code contains known security vulnerabilities when no security guidance is explicitly provided.

Three structural reasons explain the plateau:

1. **Training data.** Until models train on corpora that prioritize secure code, security performance will not improve. Public repositories are full of decades-old insecure patterns.
2. **Market incentives.** The race to build faster coding assistants has treated security as secondary. Speed to working code is not speed to secure code.
3. **Architectural limitations.** Complex dataflow analysis required for XSS and injection detection remains beyond current LLM architectures. Pattern matching catches simple vulnerabilities, but interprocedural reasoning is not there yet.

Better models produce better syntax. They do not produce more secure code. Plan accordingly.

## Five CVEs That Trace Directly to AI Coding Tools

These are not theoretical. They have CVSS scores, NVD entries, and commit-level attribution.

- **CVE-2025-32711 (EchoLeak):** Zero-click indirect prompt injection exfiltrated data from Microsoft 365 Copilot with no user interaction. CVSS 9.3. All M365 Copilot tenants were exposed pre-patch. A malicious email reaching Copilot's retrieval scope triggered exfiltration of chat logs, OneDrive files, SharePoint content, and Teams messages.

- **CVE-2025-8217 (Amazon Q Developer):** A prompt-injection payload was submitted via pull request to the public aws-toolkit-vscode repo, instructing Amazon Q to delete local files, S3 buckets, EC2 instances, and IAM users. It shipped in the official marketplace release (v1.84.0). Catastrophe was avoided only because the malicious prompt contained a syntax error.

- **CVE-2025-54135 (CurXecute, Cursor IDE):** Untrusted data from MCP servers could instruct Cursor to rewrite its own configuration and execute attacker-controlled binaries. Demonstrated end-to-end: attacker posts a crafted Slack message, user asks Cursor to summarize, RCE on developer machine. CVSS 8.6.

- **CVE-2025-54136 (MCPoison, Cursor):** After a user approved an MCP server once, the configuration could be silently swapped with a malicious version with no re-approval. CVSS 7.2. Ideal for supply-chain backdoors in team-shared repositories.

- **CVE-2025-53773 (GitHub Copilot):** Hidden prompt injection in pull request descriptions enabled remote code execution through GitHub Copilot. CVSS 9.6.

Georgia Tech's Vibe Security Radar tracked 74 confirmed AI-attributed CVEs through March 2026, with the monthly count accelerating from 6 in January to 35 in March. The project lead notes these numbers are conservative -- Claude Code appears most frequently because it "always leaves a signature," while Copilot inline suggestions leave no trace.

## What Actually Works: Inline Governance Patterns

The good news: the mitigations are not exotic. They are disciplined application of controls your team likely already understands, applied at the right enforcement points.

### Pre-commit hooks with teeth

Block commits containing credential patterns (AWS keys, Azure connection strings, API tokens) before they reach the remote. Apiiro found Azure credentials exposed nearly twice as often in AI-generated code. A regex-based pre-commit hook catches what the model does not think to redact. This is not new -- but with AI-generated code, the frequency of credential leakage makes it non-optional.

### Output validation gates in CI

Do not rely on the developer to review AI-generated code for security. Insert automated SAST and SCA scans as blocking gates in CI. When 25.1% of AI output contains confirmed vulnerabilities, manual review alone is statistically insufficient. Treat AI-generated PRs the same way you treat third-party library updates: scan, gate, and require explicit sign-off.

### Scope constraints on AI agents

The CVEs above share a common pattern: AI agents with excessive filesystem, network, or configuration access. Enforce least-privilege on coding agents. Restrict MCP server connections to an approved registry. Block self-modification of agent configuration files. The CurXecute and MCPoison vulnerabilities both exploited the absence of these boundaries.

### Credential regex and secrets scanning

Run secrets scanning on every PR, not just periodic sweeps. AI models trained on public repositories will reproduce credential patterns from training data. Scanning must be continuous because AI generation is continuous.

### Dependency verification

AI models hallucinate package names at a measurable rate. Academic research on 576,000 LLM-generated code samples found approximately 20% referenced non-existent packages, with 43% of hallucinated names repeating predictably across queries. Verify every dependency against your approved registry before installation. The slopsquatting attack surface is real and deterministic.

## The Visibility Problem

**81% of organizations lack visibility into how AI is actually used in their codebases** (Cycode 2026). You cannot govern what you cannot see. If your AppSec program does not have instrumentation showing which PRs contain AI-generated code, which models generated them, and what prompts produced them, your risk surface is unknown.

**42% of all code is now AI-generated or AI-assisted** (Sonar 2026 survey, n=1,100+). That percentage is climbing. Your scan results are going to keep getting worse unless governance is built into the generation pipeline, not bolted on after the fact.

## What to Do Monday Morning

1. **Audit your current AI tool inventory.** Which teams are using which tools? What access do those tools have? Start with `git log` attribution where possible.
2. **Add blocking SAST gates to CI for AI-generated PRs** if you do not already have them. Treat the 25.1% vulnerability rate as your baseline assumption.
3. **Deploy pre-commit credential scanning** with patterns covering cloud provider keys, connection strings, and API tokens.
4. **Restrict MCP server connections** to an approved, integrity-checked list. Review the CurXecute and MCPoison advisories for your tool chain.
5. **Establish dependency verification** against your approved package registry for every AI-suggested import.

---

**Assess your AI governance readiness:** [hummbl.io/readiness](https://hummbl.io/readiness)
**Track AI security incidents as they emerge:** [hummbl.io/tracker](https://hummbl.io/tracker)
**Evidence pack (all cited sources, structured):** [github.com/hummbl-dev](https://github.com/hummbl-dev)

---

*Sources: AppSec Santa 2026 (534 samples, 6 LLMs); Veracode 2025 GenAI Code Security Report; Veracode Spring 2026 State of Software Security; Apiiro Fortune 50 Research (Sept 2025); CodeRabbit Analysis 2026; Cycode AI Security Report 2026; Georgia Tech Vibe Security Radar (March 2026); Sonar Developer Survey 2026; NVD entries for CVE-2025-32711, CVE-2025-8217, CVE-2025-54135, CVE-2025-54136, CVE-2025-53773.*
