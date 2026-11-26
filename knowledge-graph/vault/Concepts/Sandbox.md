---
id: "concept:sandbox"
type: concept
name: Sandbox
canonical: true
category: "Agents & tools"
taught_in: 3
community: 14
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/14
source: ai-engineering-from-scratch/glossary/terms.md
---

# Sandbox

**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]]

**What it actually means:** An isolated execution environment that restricts an agent's access to files, processes, network destinations, credentials, and host resources.

**Why it matters:** Generated code and tool calls can be wrong or malicious. Isolation limits their reach and makes disposable verification practical.

**In practice:** Run tests in an ephemeral container with a read-only base, a scoped writable workspace, no production secrets, and an explicit network allowlist.

**Common confusion:** A sandbox reduces impact. It does not establish that the code inside is correct or harmless.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent Harness|Agent Harness]]
- [[Concepts/Approval Gate|Approval Gate]]
- [[Concepts/Coding Agent|Coding Agent]]
- [[Concepts/Defense in Depth|Defense in Depth]]
- [[Concepts/Guardrails|Guardrails]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Prompt Injection|Prompt Injection]]
- [[Concepts/Skill Invocation|Skill Invocation]]
- [[Concepts/Threat Model|Threat Model]]
- [[Concepts/Trust Boundary|Trust Boundary]]

## Taught in

- [[Lessons/13-26 Skill Permissions, Sandboxes, and Trust|13/26 Skill Permissions, Sandboxes, and Trust]] — An execution environment restricting reachable files, processes, network, credentials, and resources
- [[Lessons/14-29 Production Runtimes- Queue, Event, Cron|14/29 Production Runtimes: Queue, Event, Cron]]
- [[Lessons/19-05 Capstone 05 — Autonomous Research Agent (AI-Scientist Class)|19/05 Capstone 05 — Autonomous Research Agent (AI-Scientist Class)]] — Container with no network, bounded CPU/memory, pinned seeds, read-only inputs


%% ── my notes ── %%
