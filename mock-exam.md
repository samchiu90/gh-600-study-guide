# GH-600 Mock Exam (Practice Only)

> **41 questions** weighted to the official domain percentages. Time yourself: **90 minutes** (vs. the 120-minute real exam). Passing target: **29/41 ≈ 70%**.
>
> ⚠️ These questions are **constructed from the published skills outline** — they do not reproduce or paraphrase any actual exam item. They test the same competencies in plausible scenarios. Microsoft prohibits sharing real exam content (NDA), and any vendor claiming "real questions" is selling stolen or fabricated material.
>
> Question style follows Microsoft conventions: scenario-led, single best answer unless noted, plausible distractors. Where you see "(Select Y/N for each)", treat each statement independently.

---

## Domain 1 — Prepare agent architecture & SDLC processes (Q1–7)

**1.** Your team is integrating a Copilot custom agent that produces draft refactors. Reviewers complain that they can't tell *what the agent intended* before code changes appear in a PR. Which configuration most directly addresses the complaint?

- A. Increase the agent's autonomy level so it produces more diff context per PR.
- B. Configure the agent to output a structured plan as a workflow artifact before any code changes are written.
- C. Require two CODEOWNER approvals on every agent-authored PR.
- D. Reduce the agent's tool list to read-only operations.

---

**2.** Which of the following is an anti-pattern when integrating an agent into the SDLC? (Select **all** that apply.)

- A. The agent acts immediately without producing an inspectable plan.
- B. The agent runs in a workflow with `permissions: { contents: read }`.
- C. The agent's commit author is the human who triggered the workflow.
- D. The agent operates on a feature branch protected by branch protection rules.

---

**3.** You are designing a "research → propose → apply" agent flow. Which separation produces the most inspectable workflow?

- A. One job that does all three phases sequentially with grouped logs.
- B. A planning job that uploads a plan artifact, a reviewer-approved `workflow_dispatch` to begin the action job, then an evaluation job.
- C. A single job with `if: github.actor == 'admin'` gating the action step.
- D. Three sequential jobs in the same workflow with `needs:` dependencies.

---

**4.** A regulated team is concerned about agent autonomy. Which design preserves velocity while controlling risk?

- A. Require human approval on every agent-authored PR regardless of change category.
- B. Disable agent access during business hours.
- C. Categorize actions by operational/security/compliance risk and require approval only for high-risk categories.
- D. Run agents only in a dedicated repository disconnected from production.

---

**5.** Which artifact is the most appropriate "inspectable artifact" for an agent's plan in a standard GitHub workflow?

- A. A console log line in the workflow run.
- B. An `actions/upload-artifact`-uploaded JSON or markdown plan document referenced from the PR description.
- C. An entry in an external Notion database.
- D. A comment in the agent's source code.

---

**6.** You want to define success criteria for an agent task that performs a dependency upgrade. Which combination is most robust?

- A. Tests pass; no new code scanning alerts; PR template required fields completed.
- B. The agent reports "success" in its trace log.
- C. The PR is opened within 5 minutes of triggering.
- D. A human approves the PR description.

---

**7.** Your agent occasionally takes actions that contradict its earlier plan. What is the most direct architectural fix?

- A. Increase the agent's memory window.
- B. Require the agent to re-read and acknowledge its plan artifact at the start of the action phase, and abort if action steps diverge from the plan.
- C. Switch to a more capable model.
- D. Disable retries.

---

## Domain 2 — Tool use & environment interaction (Q8–17) ★

**8.** What does an MCP server primarily provide to a Copilot custom agent?

- A. A vector database for long-term memory.
- B. A standardized protocol for exposing external tools, APIs, or data sources the agent can invoke.
- C. A replacement for GitHub Actions runners.
- D. A static prompt-template registry.

---

**9.** You configured an MCP server but the agent will not invoke it in your organization. Other agents in the org work fine. Which check should you perform **first**?

- A. Confirm the server appears on the organization's MCP allow list.
- B. Restart the runner.
- C. Increase the workflow timeout.
- D. Rotate the workflow's `GITHUB_TOKEN`.

---

**10.** What is the purpose of the GitHub **remote MCP server**?

- A. To replace local MCP servers with cloud-hosted ones for any vendor.
- B. To expose GitHub's own APIs (issues, PRs, code search) to agents through MCP.
- C. To proxy outbound network calls from the Copilot cloud agent firewall.
- D. To synchronize state between multiple Copilot subscriptions.

---

**11.** Which of the following statements about MCP allow lists are true? (Select Y/N for each.)

- (a) MCP allow lists restrict which MCP servers an organization's agents may connect to.
- (b) MCP allow lists set permission levels (read/write) for each MCP tool.
- (c) Servers not on the allow list are blocked even if explicitly referenced in an agent's config.
- (d) MCP allow lists eliminate the need for per-tool permissions in the agent's manifest.

---

**12.** You want a Copilot custom agent to be invoked from a CI workflow when a PR is opened. Which is the most direct configuration?

- A. Trigger a GitHub Actions workflow on `pull_request: [opened]` with a step that runs the agent.
- B. Configure a webhook in repository settings to call the agent's HTTP endpoint.
- C. Add the agent to the repository's CODEOWNERS file.
- D. Define the agent in `.github/dependabot.yml`.

---

**13.** Your agent must create branches and pull requests autonomously. Which **minimum** `permissions:` block in the workflow file is appropriate?

- A. `permissions: { contents: read, pull-requests: read }`
- B. `permissions: { contents: write, pull-requests: write }`
- C. `permissions: write-all`
- D. `permissions: { actions: write }`

---

**14.** A team wants to allow the Copilot cloud agent to call exactly two external APIs and nothing else. Which control should they configure?

- A. CODEOWNERS for the agent's branch.
- B. The Copilot cloud agent firewall, with an allow list of the two API hosts.
- C. Repository secret scoping.
- D. Branch protection rules on `main`.

---

**15.** An agent's tool call to a flaky external service occasionally fails. Which retry strategy is most appropriate?

- A. Retry up to 10 times immediately on any error.
- B. Bounded retries with exponential backoff, scoped to transient errors (network, rate-limit), with idempotency keys on the underlying operation.
- C. Retry once, then escalate to a human regardless of error type.
- D. Disable retries and let the workflow fail.

---

**16.** You need to scope an agent so that it can only modify a single repository, not the entire organization. Which token approach is most aligned with least-privilege?

- A. A classic personal access token with `repo` scope from the team lead.
- B. The workflow's `GITHUB_TOKEN`, which is automatically scoped to that repository.
- C. A GitHub App installation token granted at the organization level on all repositories.
- D. An OAuth token from a user with admin rights on all repos.

---

**17.** Which combination provides traceability and accountability for autonomous agent actions in a GitHub workflow?

- A. Workflow run logs + signed commits attributed to the bot identity + PR comments documenting key decisions.
- B. A single end-of-run summary email to the team.
- C. Disabling actions logs to reduce noise.
- D. Storing the agent's reasoning in a private Slack channel.

---

## Domain 3 — Memory, state, and execution (Q18–22)

**18.** Where do **long-term**, project-stable agent instructions belong?

- A. Injected into the user prompt each invocation.
- B. In `.github/copilot-instructions.md` (or `AGENTS.md`) in the repository.
- C. In an environment secret.
- D. Hard-coded into the agent's source binary.

---

**19.** An agent is configured to load the entire repository's documentation into its working context every invocation. Performance is poor and answers are diluted. Which adjustment best applies?

- A. Switch to a larger context window model.
- B. Scope memory to task-relevant information only; load only the docs referenced by the current task.
- C. Increase retries.
- D. Disable memory entirely.

---

**20.** An agent is mid-task when its workflow run is canceled. On the next invocation, you need it to resume without repeating completed steps. What pattern enables this?

- A. Increase the workflow `timeout-minutes`.
- B. Persist task progress as a durable artifact (PR checklist, state file, or issue comments), and have the agent read it at the start of each run to skip completed steps.
- C. Set `concurrency: { group: agent-task, cancel-in-progress: false }`.
- D. Use a larger runner.

---

**21.** Which of the following describes **context drift** in an extended agent execution?

- A. The agent's responses become slower over time as memory grows.
- B. The agent acts on cached or stale context that no longer matches the actual repo state.
- C. The agent's prompt template becomes too long.
- D. The workflow run consumes too much GitHub Actions quota.

---

**22.** Two agents in a workflow each maintain their own local state and reach conflicting conclusions about the current branch state. What's the fix?

- A. Give one agent priority over the other.
- B. Use a single canonical state artifact that both agents read and update through serialized writes.
- C. Run the agents in different repositories.
- D. Reduce both agents' memory to short-term only.

---

## Domain 4 — Evaluation, error analysis, and tuning (Q23–29)

**23.** Which of the following are **automated** evaluation signals you should configure for an agent's output? (Select **all** that apply.)

- A. Code scanning (CodeQL) alerts.
- B. Secret scanning results.
- C. Dependabot dependency review.
- D. Reviewer commentary in PR threads.

---

**24.** An agent's PRs frequently pass tests but introduce performance regressions on a critical path. The team wants this caught automatically before merge. Which approach is most appropriate?

- A. Ask reviewers to read every diff carefully.
- B. Add a performance benchmark step that produces a required status check; fail the check if regression exceeds threshold.
- C. Disable the agent for critical-path files.
- D. Increase test timeout values.

---

**25.** An agent's failure trace shows that it called the wrong tool for a task. Which root-cause category does this most closely match?

- A. Reasoning error.
- B. Tool misuse.
- C. Context or environment issue.
- D. Network failure.

---

**26.** After analyzing failures, you find that the agent consistently misinterprets a custom internal API because its description in the agent's config is ambiguous. What is the most appropriate tuning step?

- A. Revise the agent's tool descriptions and add usage examples in its config.
- B. Increase the agent's max-token budget.
- C. Remove the tool from the agent's available list.
- D. Switch to a different LLM provider.

---

**27.** Which of the following best aligns evaluation criteria with development intent?

- A. Use eval signals that mirror the criteria a human contributor would be judged on (tests, scans, review feedback).
- B. Define agent-only metrics like "tool calls per task" as the primary success measure.
- C. Disable code review for agent-authored PRs to measure raw agent capability.
- D. Use only the LLM's self-reported confidence score.

---

**28.** Which artifacts are most useful when diagnosing a failed agent run? (Select **all** that apply.)

- A. Workflow run logs.
- B. The agent's structured plan output.
- C. The execution trace (tool calls in order).
- D. The uploaded artifacts (intermediate state, evaluations).

---

**29.** An agent's reasoning is consistently wrong about the team's preferred coding style. Which tuning is most direct?

- A. Update the agent's custom instructions in `.github/copilot-instructions.md` with the team's style conventions.
- B. Increase the agent's autonomy level.
- C. Add a `style-check` retry loop.
- D. Reduce the agent's memory.

---

## Domain 5 — Multi-agent coordination (Q30–36)

**30.** Which pattern best describes a "supervisor" multi-agent orchestration?

- A. All agents act simultaneously and outputs are merged at the end.
- B. One agent dispatches sub-tasks to worker agents and reviews their outputs.
- C. Two agents debate and a third arbitrates.
- D. Agents are arranged in a fixed sequential pipeline.

---

**31.** You run three agents in parallel on the same repository. To prevent conflicting code changes, which approach is best?

- A. Run all three agents against the `main` branch directly.
- B. Run each agent on its own feature branch with non-overlapping file scopes, and detect conflicts at PR-merge time.
- C. Disable two of the agents and run them sequentially.
- D. Increase the runner size to handle merges.

---

**32.** Two parallel agents produce contradictory PRs that modify the same file. Which recovery pattern is most appropriate?

- A. Auto-merge both PRs.
- B. A reconciler (judge agent) with a defined arbitration rule, or human-in-the-loop review if disagreement exceeds threshold.
- C. Reject both PRs without review.
- D. Force-push to overwrite one of the branches.

---

**33.** Which artifact best supports post-hoc analysis of a multi-agent workflow?

- A. A top-level orchestration record (issue or workflow run) linking every sub-agent's run, with decision logs at handoffs.
- B. A summary log message on the orchestrator's exit.
- C. Each agent's local debug output, kept only on its runner.
- D. A Slack thread between the team's engineers.

---

**34.** Your orchestrator detects that one of three parallel agents has produced no progress for 30 minutes. What's the most appropriate first response?

- A. Allow the agent to continue indefinitely.
- B. Apply a workflow timeout, mark the run failed, and route the sub-task to a fallback path (rerun, alternative agent, or human).
- C. Increase the runner's CPU allocation.
- D. Cancel all three agents' runs.

---

**35.** You want to introduce a new agent into an existing multi-agent workflow without disrupting current runs. Which deployment is safest?

- A. Replace the existing agent immediately and roll forward.
- B. Deploy the new agent in shadow mode, run it alongside the existing one, compare outputs, then promote once parity is confirmed.
- C. Run the new agent only on weekends.
- D. Disable the existing agent for one week to validate the new one.

---

**36.** A retired agent's audit trail must remain accessible for compliance review. Which approach preserves auditability?

- A. Delete the agent's config and all associated workflow runs.
- B. Archive the config in git history, retain workflow runs/artifacts per retention policy, and document the retirement in a governance record.
- C. Move the workflow runs to a private external storage system not linked to the repository.
- D. Disable workflow logging going forward.

---

## Domain 6 — Guardrails & accountability (Q37–41)

**37.** Which action category most clearly requires explicit human authorization?

- A. Auto-formatting a markdown file.
- B. Renaming a private variable in test code.
- C. Modifying a CI/CD pipeline that deploys to production.
- D. Adding a comment to an existing issue.

---

**38.** Which mechanism most directly enforces least-privilege execution context for an agent in a workflow?

- A. A workflow `permissions:` block scoped to the minimum needed for the task.
- B. A team-wide announcement in Slack.
- C. A pinned issue describing expected behavior.
- D. A README note in the repository root.

---

**39.** You want to require approval before an agent can deploy to production but not for routine PRs. Which GitHub feature is most appropriate?

- A. Branch protection rules on `main`.
- B. An environment with required reviewers attached to the production deploy job.
- C. CODEOWNERS for the entire `src/` directory.
- D. A `WORKING-HOURS` setting on the repository.

---

**40.** Which of the following minimize approval friction *without* reducing safety? (Select **all** that apply.)

- A. Require approval only for irreversible or compliance-sensitive changes.
- B. Use CODEOWNERS on sensitive paths so reviews are targeted, not global.
- C. Require two reviewers on every PR including doc typos.
- D. Use environment protection rules so prod deploys are gated but dev flows freely.

---

**41.** An agent is about to perform an irreversible production change (e.g., dropping a database column). Which set of controls is the **best** combination?

- A. CODEOWNERS approval on the migration file + environment protection rule with required reviewers on the prod environment + a structured plan artifact reviewed before the action job runs.
- B. A retry loop with exponential backoff.
- C. A larger workflow `timeout-minutes` value.
- D. Allow the agent to proceed and revert later if needed.

---

# Answer Key & Explanations

| # | Answer | Why |
|---|---|---|
| 1 | **B** | Reviewers' complaint is about *visibility before code*. A structured plan artifact published before any change addresses that exactly. CODEOWNER counts (C) gate merge but don't show intent earlier; (A) is opposite of the issue; (D) discards capability. |
| 2 | **A** | Acting without an inspectable plan is the canonical anti-pattern. (B) is fine (read-only is safe), (C) is acceptable when the human triggers it, (D) is good practice. |
| 3 | **B** | Separation of plan/approve/act/evaluate into discrete artifact-producing steps is the inspectability pattern. (A) groups logs but doesn't gate; (C) is identity gating only; (D) sequential jobs alone don't add approval gates. |
| 4 | **C** | Risk-tiered autonomy is the published guidance. (A) is approval theater; (B)(D) reduce velocity without proportionate safety gain. |
| 5 | **B** | A workflow artifact referenced from the PR is the canonical inspectable artifact. (A) is ephemeral, (C) is off-platform, (D) isn't an artifact. |
| 6 | **A** | Multiple objective criteria mirroring human-contributor judgment. (B) is self-reported, (C) measures speed not quality, (D) is subjective. |
| 7 | **B** | Plan/action divergence is fixed by making the plan a hard contract, not by upgrading the model or memory. |
| 8 | **B** | MCP is the standardized tool-exposure protocol. (A) is wrong (memory is separate), (C) is wrong (MCP doesn't replace runners), (D) is wrong. |
| 9 | **A** | Allow-list misses are the most common cause when other agents work. Always check the allow list before deeper debugging. |
| 10 | **B** | The GitHub remote MCP server exposes GitHub's APIs as MCP tools. |
| 11 | **Y, N, Y, N** | (a) Yes — that's its purpose. (b) No — permissions live in agent/tool config, not allow lists. (c) Yes — allow lists are enforced regardless of agent intent. (d) No — per-tool permissions still apply within an allowed server. |
| 12 | **A** | Standard GitHub Actions trigger pattern. (B) is custom plumbing, (C) doesn't run code, (D) is for dependency updates only. |
| 13 | **B** | Minimum needed to create branches and PRs. (A) is read-only, (C) is broader than needed, (D) is for managing workflows. |
| 14 | **B** | The Copilot cloud agent firewall is the named control for egress allow-listing. |
| 15 | **B** | Standard safe-retry pattern: bounded, backoff, idempotency, scoped to transient errors. |
| 16 | **B** | `GITHUB_TOKEN` is the textbook least-privilege option for in-repo work. (A) over-scopes by user, (C) over-scopes by org, (D) is far too broad. |
| 17 | **A** | The three-pillar pattern: logs, attribution, and decisional comments. |
| 18 | **B** | Repo-level instructions file is the canonical home for stable long-term agent guidance. |
| 19 | **B** | Scope memory to task-relevant — published Domain 3 bullet. Bigger windows and more retries don't fix dilution. |
| 20 | **B** | Durable progress artifact pattern is the published resumption mechanism. |
| 21 | **B** | Context drift specifically = action-state divergence; the others are unrelated performance/scale issues. |
| 22 | **B** | Single source of truth + serialized writes is the canonical fix. |
| 23 | **A, B, C** | All three are automated scanners. (D) is human input, not automated. |
| 24 | **B** | Required status check on a benchmark is the standard gate. (A) doesn't scale, (C) over-restricts, (D) hides the regression. |
| 25 | **B** | Wrong tool call = tool misuse by definition. |
| 26 | **A** | Tune by revising tool descriptions/examples. (B)(D) are unrelated; (C) discards capability. |
| 27 | **A** | Alignment with contributor judgment criteria is the published principle. |
| 28 | **A, B, C, D** | All four are the listed diagnostic surfaces. |
| 29 | **A** | Custom instructions are the canonical home for team conventions. |
| 30 | **B** | Supervisor = dispatch + review. (A) is fan-out/fan-in, (C) is debate/critic, (D) is sequential pipeline. |
| 31 | **B** | Branch isolation + file-scope separation + PR-time conflict detection is the parallel-agent pattern. |
| 32 | **B** | Reconciler agent or human-in-the-loop is the published recovery pattern. |
| 33 | **A** | Linked orchestration record with handoff logs is the auditable structure. |
| 34 | **B** | Timeout + fallback path is the standard stalled-execution response. |
| 35 | **B** | Shadow-mode parity check is the safe rollout. |
| 36 | **B** | Archive in git + retain runs + document = audit-trail preservation. |
| 37 | **C** | Production CI/CD changes are explicitly the high-risk category. |
| 38 | **A** | Workflow `permissions:` block is the GitHub primitive for least privilege at execution time. |
| 39 | **B** | Environment protection rules with required reviewers are the named gate for deploys. |
| 40 | **A, B, D** | All target risk-proportionate approval; (C) is approval theater that adds friction without proportionate safety. |
| 41 | **A** | Defense-in-depth: code-level review (CODEOWNERS) + deploy-gate (environment) + intent review (plan artifact). |

---

## Scoring guide

| Score | Reading |
|---|---|
| 36–41 (~88%+) | Strong — schedule the beta. |
| 29–35 (~70–85%) | Borderline — review wrong answers, especially in your weakest domain. |
| Under 29 | Spend another 1–2 weeks on the modules and gap docs; resit this mock cold. |

For every miss: copy the question into `knowledge-gaps.md`, write the *correct* reasoning (not just the letter), and revisit it the next day.
