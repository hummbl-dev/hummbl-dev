# Slop Tracker Welcome Sequence -- 5 Emails Over 14 Days

**Trigger**: New subscriber to AI Slop Tracker newsletter OR completion of /readiness governance assessment
**Sender**: reuben@hummbl.io
**From name**: Reuben at HUMMBL
**Unsubscribe**: One-click, every email

---

## Evidence posture

This is a **conversion email sequence**, not a primary-source bundle or legal/compliance advisory.

- It compresses research claims into persuasive outreach copy.
- Strong numeric, insurance, and legal statements should be rechecked against the current research corpus before external deployment.
- Urgency and certainty in subject lines or CTAs are conversion choices, not standalone evidence.

See [README.md](README.md) in this folder and [`../../PROOF_AND_RESEARCH_EVIDENCE_POSTURE.md`](../../PROOF_AND_RESEARCH_EVIDENCE_POSTURE.md).

---

## Email 1 -- Day 0: Welcome

**Subject**: Your first AI Slop Tracker issue
**Preview text**: The weekly evidence digest for AI governance leaders

**Body**:

You signed up for the AI Slop Tracker. Here is what you will get every week:

- 3-5 verified AI governance incidents, with source links
- Regulatory updates (EU AI Act, state-level, sector-specific)
- One data point from the vulnerability research, contextualized

No predictions. No hype. Claims are intended to be source-traceable through the research corpus.

Your first issue is live: [Read Issue #1 here]

If you completed the readiness assessment, your results are in your inbox separately. That score is your baseline. We will reference it in a few days.

-- Reuben

**CTA**: Read Issue #1 (button, links to latest newsletter)

---

## Email 2 -- Day 3: The One Stat

**Subject**: 2.74x more vulnerable
**Preview text**: AI-generated code vs human-written, by the numbers

**Body**:

Veracode's 2025 analysis found that AI-generated code was reported as 2.74 times more vulnerable than human-written code. Not 10% worse. Not marginally riskier. Nearly three times the vulnerability rate, based on that benchmark.

This number holds even as models improve. Veracode's Spring 2026 follow-up shows security pass rates stuck at roughly 55% for two years straight. The models get better at generating code. They do not get better at generating secure code.

Why this matters to you: if 42% of your codebase is now AI-generated (the industry average per Sonar's 2026 survey of 1,100+ developers), your attack surface has expanded by a factor you have never measured.

The full breakdown, with methodology and caveats, is on our blog.

-- Reuben

**CTA**: Read the full analysis (links to CISO-targeted blog post)

---

## Email 3 -- Day 7: The Insurance Problem

**Subject**: Your D&O policy may not cover this
**Preview text**: Berkley's AI exclusion changes the math

**Body**:

W.R. Berkley has introduced broad AI exclusions on Directors & Officers and Errors & Omissions policies. Not sublimits. Not higher premiums. Broad exclusions that make documented governance posture materially more important.

Other carriers are watching. If major AI-related D&O claims continue to mature, carriers without exclusions may follow Berkley's lead. Moffatt v. Air Canada and Mobley v. Workday are part of that legal-risk signal, not a guarantee of identical downstream outcomes.

The practical effect: insurance is becoming a de-facto AI governance enforcement mechanism. Your underwriter will ask what controls you have before your regulator does.

The question is whether you can show evidence of governance at renewal time.

-- Reuben

**CTA**: Read the risk manager's guide (links to Risk Manager blog post)

---

## Email 4 -- Day 10: The 90-Day Playbook

**Subject**: 90 days to defensible AI governance
**Preview text**: A concrete roadmap, not a framework deck

**Body**:

You do not need a 12-month transformation program to establish defensible AI governance. You need 90 days and four deliverables:

**Days 1-30**: Inventory. Which teams use AI agents? What can those agents access? Where does AI-generated code land in production? You cannot govern what you have not mapped.

**Days 31-60**: Controls. Kill switches on agent operations. Circuit breakers on external integrations. Scope limits enforced by tooling, not policy. Append-only audit logs capturing who authorized what.

**Days 61-90**: Evidence. Demonstrate to your board, your insurer, and your regulator that you have runtime governance producing continuous compliance evidence. Not a point-in-time assessment. A living system.

We wrote the detailed playbook -- specific tools, specific milestones, specific evidence artifacts -- for AI Governance Leads. It is the most practical thing we have published.

If you took the readiness assessment on Day 0, revisit your score. The playbook maps directly to the gaps it identified.

-- Reuben

**CTA**: Get the 90-day playbook (links to AI Governance Lead blog post + readiness assessment)

---

## Email 5 -- Day 14: Ready to Talk?

**Subject**: One question for you
**Preview text**: Where are you on the governance timeline?

**Body**:

You have been reading the Slop Tracker for two weeks. You have seen the vulnerability data, the insurance exclusions, the regulatory timeline, and the 90-day playbook.

Here is the one question that matters: do you have runtime evidence of AI governance today, or are you reconstructing it after something goes wrong?

If the answer is "not yet," that is normal. Most organizations are in the same position. The EU AI Act enforcement begins August 2, 2026. Carrier renewals happen on their own schedule. The window to build defensible governance before you need it is closing, but it is not closed.

We help organizations stand up AI governance on a shorter timeline than a traditional transformation program. Stdlib-only tooling. No SaaS dependency. Evidence-oriented controls designed to support framework mapping and insurer/regulator conversations.

If you want to talk about what this looks like for your organization, pick a time or reply to this email.

-- Reuben

**CTA**: Book a 30-minute call (links to Cal.com booking page)

**Secondary link**: Or email reuben@hummbl.io directly

---

## Sequence Notes

**Timing**: Emails send at 9:00 AM in the subscriber's local timezone. If timezone is unknown, default to 9:00 AM ET.

**Suppression rules**:
- If subscriber books a call (Email 5 CTA) before Day 14, suppress remaining emails and move to sales sequence.
- If subscriber opens zero emails after Email 2, pause sequence and send a re-engagement email at Day 21.
- If subscriber completes the readiness assessment after Day 0, send a one-time results email outside this sequence.

**Metrics to track**:
- Open rate per email (benchmark: 35%+ for niche B2B)
- Click rate on primary CTA (benchmark: 5%+)
- Assessment completions driven by Email 4
- Calls booked from Email 5
- Sequence completion rate (all 5 opened)

**A/B test candidates**:
- Email 2 subject: "2.74x more vulnerable" vs "The number your CISO needs to see"
- Email 5 subject: "One question for you" vs "The window is closing"
- Email 3 CTA: blog link vs direct readiness assessment link
