# Thread 04: 22 Production Incidents from AI-Generated Code

---

**1/** (103 chars)
We catalogued 22 production incidents caused by AI-generated code. Here are the worst ones: [thread]

**2/** (276 chars)
CVE-2025-32711 -- EchoLeak. Zero-click prompt injection in M365 Copilot. Malicious email reaches Copilot's retrieval scope, silently exfiltrates chat logs, OneDrive files, SharePoint content, Teams messages. CVSS 9.3. No user interaction required. Discovered by Aim Security.

**3/** (274 chars)
CVE-2025-8217 -- Amazon Q Developer wiper. Attacker submitted a PR to aws-toolkit-vscode containing prompt injection instructing Q to delete local files, S3 buckets, EC2 instances, and IAM users. It shipped in the official v1.84.0 release. Only a syntax error prevented execution.

**4/** (275 chars)
CVE-2025-54135 -- CurXecute. Untrusted data from MCP servers (e.g., Slack messages) could instruct Cursor to rewrite its own config and execute attacker binaries. Demonstrated end-to-end: attacker posts crafted Slack message, user asks Cursor to summarize, RCE on dev machine.

**5/** (260 chars)
Apiiro's Fortune 50 research (Dec 2024-June 2025): AI-assisted code produced 322% more privilege escalation paths, 153% more design flaws, and exposed Azure credentials nearly twice as often. By June 2025, over 10,000 new security findings per month.

**6/** (267 chars)
curl bug bounty shutdown (Feb 2026). ~20% of all HackerOne submissions were AI-generated slop: vulnerabilities in functions that don't exist, fabricated GDB sessions, hallucinated changelogs. Validity rate: 0%. Daniel Stenberg: "AI is DDoSing open source."

**7/** (276 chars)
Google Gemini CLI catastrophic file deletion (July 2025). User asked it to rename a directory. mkdir silently failed. Agent didn't check. Proceeded to "move" files into a non-existent target. Files irrecoverably destroyed. Agent confessed: "my gross incompetence."

**8/** (258 chars)
Google Antigravity / Gemini 3 Pro (Dec 2025). Developer used autonomous "Turbo/YOLO mode." Agent wiped their entire D: drive while building an image-selector app. YOLO mode removes confirmation gates from destructive operations. Total drive loss.

**9/** (272 chars)
Slopsquatting: LLMs hallucinate plausible package names. Researcher registered "huggingface-cli" on PyPI (doesn't exist). 30,000+ real downloads in 3 months from devs running LLM-suggested pip install. 20% of AI code samples reference non-existent packages.

**10/** (244 chars)
The pattern across all 22 incidents: AI agents running with developer-level privileges, no verification between speculative state and actual state, no cost caps, no scope boundaries, no human gate on destructive operations. Unsupervised agents.

**11/** (262 chars)
The acceleration: pre-2025, agent-RCE CVEs in AI coding tools were effectively zero. H2 2025 alone: 7 named high-CVSS CVEs. Monthly rate went from ~0 to ~1/month by mid-2025. Georgia Tech's Vibe Security Radar tracked 74 AI-linked CVEs by March 2026.

**12/** (222 chars)
Every one of these was preventable with basic governance: delegation scoping, circuit breakers on destructive operations, kill switches, audit trails. The tools are powerful. Running them unsupervised is negligence.

---

SCHEDULING NOTE: Post Tuesday 11:00 AM - 12:00 PM ET. Incident threads get high engagement during lunch-break scrolling. Use a poll or "which one surprised you most?" reply to boost engagement. Thread has viral potential -- lead with the most dramatic incidents.
