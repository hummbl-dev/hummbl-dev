# Round 4: MCP Governance as a HUMMBL Wedge

**Lane:** MCP (Model Context Protocol) governance and security risks
**Date:** 2026-04-05
**Verdict:** YES — MCP governance is a real and sharpening wedge. Positioning angle below.

---

## 1. MCP Adoption State (2024–2026)

MCP moved from an Anthropic side-release (Nov 2024) to a de facto industry standard in ~14 months. Key signals:

- **Registry scale.** The official MCP Registry (launched Sept 2025) hosts ~2,000 vetted entries and has grown 407% since launch. The broader third-party ecosystem is roughly 5× larger: **Glama's directory lists 20,249 servers as of March 2026**, and aggregators estimate **10,000+ active public MCP servers** [[MCP Anniversary Post]](https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/) [[Glama via WorkOS]](https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026).
- **SDK pull.** Python + TypeScript MCP SDKs exceed **97M downloads per month** combined.
- **Client integration.** Claude Desktop, Cursor, Zed, VS Code, **ChatGPT, Gemini, and Microsoft Copilot** all ship MCP client support by Q1 2026 [[MCP Registry docs]](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/).
- **Governance handoff.** In **December 2025 Anthropic donated MCP to the Agentic AI Foundation (Linux Foundation)** — the protocol is now vendor-neutral, which accelerates enterprise adoption but *removes Anthropic as a single throat-to-choke for security vetting* [[Anthropic]](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation).
- **Enterprise signals.** Fortune 500 deployments are publicly referenced; WorkOS, Stripe, GitHub, Linear, Atlassian, Notion, Slack, HubSpot all publish first-party MCP servers.

**Takeaway:** Adoption is not speculative. It is at Docker-2015 / npm-2012 scale — ubiquitous but under-governed.

---

## 2. Documented MCP Security Risks

The risk landscape in 2025–2026 is **large, growing, and poorly contained.** The line "one compromised MCP connection enables credential exfiltration that no static scanner will catch" is conservative.

### 2a. Published CVEs & breaches

| Vuln | Impact | Source |
|---|---|---|
| CVE-2025-6514 (`mcp-remote`) | Critical OS command injection in the most-used OAuth proxy for remote MCP | JFrog |
| Anthropic MCP Inspector RCE | Unauthenticated RCE just by inspecting a malicious server | authzed timeline |
| CVE-2025-68143/68144/68145 | Chained RCE via `mcp-server-git` + Filesystem MCP through malicious `.git/config` | Anthropic advisory |
| `postmark-mcp` (npm, Sept 2025) | **First confirmed malicious MCP server**: one-line BCC backdoor exfiltrated thousands of emails; ~300 orgs compromised | Snyk, Koi Security |

[[Timeline of MCP breaches]](https://authzed.com/blog/timeline-mcp-breaches) [[Snyk postmark-mcp]](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/)

### 2b. Tool Poisoning / Prompt Injection

Coined by **Invariant Labs (April 2025)**. Malicious instructions are hidden in tool descriptions or JSON schemas — visible to the model, invisible to the user [[Invariant Labs]](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks). Demonstrated attacks:

- **WhatsApp exfiltration** — a benign "fact-of-the-day" tool later mutated its description to BCC all WhatsApp messages to an attacker number.
- **Tool shadowing** — a malicious server rewrites the behavior of a *different trusted* server's tools (e.g., `send_email`) at runtime.
- **Rug-pull / mutable definitions** — tool definitions approved at install time silently change after first use.

### 2c. Benchmarked prevalence

- **MCPTox** (arXiv 2508.14925, Aug 2025): 45 real MCP servers, 353 tools, 1,312 malicious test cases. **Attack success rates >60% on o1-mini and DeepSeek-R1; Claude-3.7-Sonnet refused <3%.** Safety alignment is ineffective against tool poisoning [[MCPTox]](https://arxiv.org/abs/2508.14925).
- **MCPSecBench** (arXiv 2508.13220) + **MCP-SafetyBench** (arXiv 2512.15163) corroborate.
- **March 2025 audit** of public MCP implementations: **43% had command-injection flaws; 30% permitted unrestricted URL fetches** [[Practical DevSecOps]](https://www.practical-devsecops.com/mcp-security-vulnerabilities/).
- "Trivial Trojans" (arXiv 2507.19880) — minimal MCP servers can exfiltrate via legitimate tools.

### 2d. Supply chain & shadow MCP

- **Typosquatting on npm/PyPI** is the dominant attack vector; MCP servers look like normal deps.
- **Shadow MCP** (OWASP MCP09:2025) — devs install MCP servers via `claude_desktop_config.json` or `.cursor/mcp.json` **without SecOps visibility**. Servers run on localhost and do not touch SIEM [[OWASP Shadow MCP]](https://owasp.org/www-project-mcp-top-10/2025/MCP09-2025%E2%80%93Shadow-MCP-Servers).
- **No registry-level signing or attestation** yet enforced; the official registry has *preview* vetting but third-party directories (Glama, Smithery) do not.

---

## 3. Academic / Community Coverage

- **OWASP MCP Top 10 (2025)** — dedicated project, independent of the LLM Top 10 [[OWASP MCP Top 10]](https://owasp.org/www-project-mcp-top-10/).
- **OWASP Agentic Top 10 for 2026** — ASI04 "Agentic Supply Chain Vulnerabilities" explicitly calls out MCP servers as attack surface and recommends SBOMs for tools/models [[OWASP Gen AI]](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).
- **Simon Willison (Apr 2025)** — widely cited post framing MCP prompt injection as structural, not a bug [[Simon Willison]](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).
- **Elastic Security Labs, CyberArk, Checkmarx Zero, Palo Alto Unit42, Red Hat, eSentire** all published MCP threat primers in 2025.
- **arXiv:** at least 4 benchmark papers (MCPTox, MCPSecBench, MCP-SafetyBench, Trivial Trojans) — a credible academic base.

---

## 4. Existing MCP Governance Tooling (Competitive Landscape)

**First-party (Anthropic / MCP org):**
- **MCP Inspector** — developer debugger (itself had an RCE CVE).
- **Official Registry** — preview-grade vetting, no signing enforcement yet.
- Protocol validators in SDKs.

**Security scanners:**
- **Invariant Labs `mcp-scan`** (now rebranded as part of **Snyk `agent-scan`**) — static analysis of tool schemas for poisoning patterns.
- **Cisco AI Defence MCP Scanner** — registration-time + periodic scans.
- **Semgrep rules** for MCP anti-patterns.

**Gateways / policy proxies (crowded):**
- **Lasso Security MCP Gateway** (open source)
- **MintMCP, MCP Manager, Composio, TrueFoundry, Integrate.io, Acuvity, Maxim, Netskope, Zscaler**
- **agentic-community/mcp-gateway-registry** (OAuth + Keycloak/Entra)

**Enterprise management:** at least **10+ commercial MCP gateways** shipping by Q1 2026 per Composio's comparison. The *gateway* segment is crowding fast. The *governance primitives* segment (audit, attestation, capability tokens) is less crowded.

---

## 5. HUMMBL Wedge Opportunity

### Where the gap actually is

The gateway market is saturated. The scanner market has incumbents (Snyk, Cisco, Semgrep). But three gaps are visible:

1. **Capability attestation & signed tool schemas** — no one has shipped a widely-adopted signing standard. Tool-poisoning is possible because schemas are unsigned, mutable, and invisibly modifiable at runtime. An *attestation primitive* (signed schema + pinned hash + governance bus receipt on change) is the natural extension of HUMMBL's IDP work.
2. **Cross-server flow integrity** — tool shadowing attacks exploit *trust between* servers. No one today enforces "server A may not describe tools that override server B." This is a Base120-style orthogonality problem.
3. **Governance log for individual / small-team devs** — enterprise gateways solve for CISOs. Solo devs and 2–10-person teams (the HUMMBL audience) have **zero governance primitives**; they run `claude_desktop_config.json` with 8 servers and no audit trail.

### Why HUMMBL is credibly positioned

- **Stdlib-only + append-only JSONL governance bus** already matches the "lightweight, local, auditable" shape MCP needs.
- **IDP Phase 0** (HMAC-signed delegation tokens, capability chains, DCTX depth enforcement) is *directly applicable* to MCP tool invocations. Reframing IDP as "MCP capability attestation" is a 2-week repositioning.
- **Base120 MCP server** itself dogfoods the story: "We publish an MCP server and we govern it."

### Who buys

- **Primary:** security-conscious **individual developers and small teams (2–10)** running Claude Desktop / Cursor with 5+ MCP servers — they already feel the pain and have no enterprise gateway budget.
- **Secondary:** **platform/security engineers at AI-native startups** (50–200 people) who need governance but not a $50k/yr Cisco deployment.
- **NOT:** Fortune 500 CISOs (crowded, slow sales cycle, incumbents winning).

### Positioning line

> **"Governance primitives for MCP-native agent systems — attestation, capability tokens, and audit receipts that run locally, stdlib-only, and survive the rug-pull."**

This is sharper than "MCP security" (crowded) and sharper than "agent governance" (vague). It names the artifact (primitives), the consumer (MCP-native devs), and the differentiator (local + stdlib + receipts).

---

## Sources

- [MCP Anniversary Post](https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/)
- [Anthropic — Donating MCP to Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [MCP Registry Preview](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/)
- [WorkOS — Everything about MCP in 2026](https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026)
- [Timeline of MCP Security Breaches — Authzed](https://authzed.com/blog/timeline-mcp-breaches)
- [Vulnerable MCP Project](https://vulnerablemcp.info/)
- [Invariant Labs — Tool Poisoning](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Simon Willison — MCP Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Elastic Security Labs — MCP Attack Vectors](https://www.elastic.co/security-labs/mcp-tools-attack-defense-recommendations)
- [Snyk — Malicious postmark-mcp](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/)
- [Acuvity — One Line of Code](https://acuvity.ai/one-line-of-code-thousands-of-stolen-emails-the-first-malicious-mcp-server-exposed/)
- [Semgrep — First Malicious MCP on npm](https://semgrep.dev/blog/2025/so-the-first-malicious-mcp-server-has-been-found-on-npm-what-does-this-mean-for-mcp-security/)
- [MCPTox arXiv 2508.14925](https://arxiv.org/abs/2508.14925)
- [MCPSecBench arXiv 2508.13220](https://arxiv.org/html/2508.13220v2)
- [Trivial Trojans arXiv 2507.19880](https://arxiv.org/html/2507.19880v1)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- [OWASP Shadow MCP Servers](https://owasp.org/www-project-mcp-top-10/2025/MCP09-2025%E2%80%93Shadow-MCP-Servers)
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [Practical DevSecOps — MCP Vulnerabilities](https://www.practical-devsecops.com/mcp-security-vulnerabilities/)
- [eSentire — MCP Security for CISOs](https://www.esentire.com/blog/model-context-protocol-security-critical-vulnerabilities-every-ciso-should-address-in-2025)
- [Checkmarx Zero — 11 Emerging MCP Risks](https://checkmarx.com/zero-post/11-emerging-ai-security-risks-with-mcp-model-context-protocol/)
- [Red Hat — MCP Security Risks and Controls](https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls)
- [Palo Alto — Guide to MCP Vulnerabilities](https://www.paloaltonetworks.com/resources/guides/simplified-guide-to-model-context-protocol-vulnerabilities)
- [CyberArk — Poison Everywhere](https://www.cyberark.com/resources/threat-research-blog/poison-everywhere-no-output-from-your-mcp-server-is-safe)
- [Lasso Security — Open Source MCP Gateway](https://www.lasso.security/resources/lasso-releases-first-open-source-security-gateway-for-mcp)
- [Composio — 10 Best MCP Gateways 2026](https://composio.dev/content/best-mcp-gateway-for-developers)
- [Incredibuild — SBOMs for MCP Servers](https://www.incredibuild.com/blog/the-hidden-supply-chain-in-your-ai-agent-why-sboms-for-mcp-servers-matter-now)
- [Snyk agent-scan (formerly mcp-scan)](https://github.com/invariantlabs-ai/mcp-scan)
