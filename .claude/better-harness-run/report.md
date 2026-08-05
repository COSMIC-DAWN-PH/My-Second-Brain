# Better Harness Task-Loop Report

## At a Glance

- Loop Effectiveness: 47/100 (changes only after comparable later task outcomes)
- Asset Health / Repair Progress: 0/100 (0 verified, 0 partial, 5 pending)
- Demonstrated autonomy radius: not observed (not observed; not observed confidence)
- Strongest loop: Not enough evidence difference to name one.
- Largest observed leak: Use the priority moves; no single loop is uniquely weakest.
- Top expected gain: No priority benefit is available in this evidence boundary.

## What You Can Rely On Today

- No reliable user outcome has been demonstrated in this evidence boundary yet.

## What You Gain Next

- No priority Harness move is available in this evidence boundary.



### Why these moves matter

### No automated validation or dependency gates protect the plotting pipeline
- Priority: Medium · Evidence: not observed in this boundary
- Reason: The project contains Python scripts that generate figures for notes and handouts, but the bundle shows 0 test files, 0 CI configuration, no requirements.txt, and no pyproject.toml. The doc-audit skill provides a manual checklist, so a broken script, missing dependency, or malformed YAML frontmatter can be committed without any mechanical signal. This leaves the agent workflow dependent on human-triggered skills and visual inspection.
- Expected Output:
  1. A dependency manifest that an agent can install in one command.
  2. A focused test that fails when a plotting script cannot run.
  3. A documented command the next agent can run to verify the pipeline.

### Asset-generation scripts mutate the working tree without reset or verification
- Priority: Medium · Evidence: not observed in this boundary
- Reason: Handout by AI/generate_assets.py and the Rydberg atom/attachments/*.py scripts write PNG outputs into the repository at hard-coded paths. Running them changes the working tree, and there is no check that the committed PNGs are current with the scripts that produced them. An agent could regenerate assets, commit, and leave stale or unrelated images in the vault.
- Expected Output:
  1. A command that regenerates all vault assets deterministically.
  2. A command that fails if committed PNGs do not match the current scripts.
  3. A note in the project rules telling agents to run verify-assets after changing plotting code.

### Skill file naming is inconsistent with the project's own convention
- Priority: Low · Evidence: not observed in this boundary
- Reason: AGENTS.md and CLAUDE.md state that skill files are named SKILL.md (uppercase). The daily-research skill, however, exists as skill.md (lowercase) in both .claude/skills/daily-research/ and .agents/skills/daily-research/. In addition, the literature_handout skill folder does not match the skill name literature-handout declared in its YAML frontmatter. These inconsistencies can break skill discovery on case-sensitive filesystems and make the rule set self-contradictory.
- Expected Output:
  1. Every skill file is named SKILL.md.
  2. Every skill folder matches the YAML name field exactly.
  3. sync-config reports no drift between .claude/ and .agents/.

### Twin rule files require manual synchronization
- Priority: Low · Evidence: not observed in this boundary
- Reason: CLAUDE.md and AGENTS.md declare themselves as synchronized duplicate copies of vault rules, and the sync-config skill is responsible for keeping them consistent. This manual twin-file pattern is a drift risk: if one file is updated without the other, different agents or sessions will read contradictory instructions. No automated check currently blocks such divergence.
- Expected Output:
  1. One canonical rule file, or a generated second file with a documented build step.
  2. A check that fails when the two files are out of sync.

### Long skills lack progressive references
- Priority: Low · Evidence: not observed in this boundary
- Reason: The lint envelope flags doc-audit (503 lines), learning-path (263 lines), literature_handout (314 lines), sync-config (351 lines), and zotero-notes (250 lines) as having no local Markdown references. Single-file skills of this length are harder to maintain and load into context efficiently. The doc-audit skill in particular exceeds the hard-cap threshold and is the only warning in the lint envelope.
- Expected Output:
  1. Each SKILL.md is under 200 lines.
  2. Detailed procedures live in sibling .md files referenced by the SKILL.md.
  3. The skill triggers and expected artifacts remain discoverable.

## Five Lifecycle Dimensions

| Dimension | What the evidence proves | Evidence boundary | Summary | Boundary / blocker |
| --- | --- | --- | --- | --- |
| Task Understanding | Not observed yet | not observed in this boundary | AGENTS.md and CLAUDE.md give clear vault conventions, but the twin-file sync rule and skill-name/filename inconsistencies create ambiguity about the authoritative source. | not observed |
| Controlled Execution | Not observed yet | not observed in this boundary | Asset scripts exist, yet there is no dependency manifest, doctor command, or documented reset path, and the skill tree has a casing mismatch. | not observed |
| Change Validation | Not observed yet | not observed in this boundary | The doc-audit skill supplies a thorough manual checklist, but no automated tests, CI, or affected-check routing verify edits. | not observed |
| Reliable Delivery | Not observed yet | not observed in this boundary | Git history is present and the working tree is clean, but there is no PR/merge workflow or automated recovery path. | not observed |
| Learning Capture | Not observed yet | not observed in this boundary | Skills are configured, but no session evidence is available to show they are invoked, validated, or improving later outcomes. | not observed |

## The 15 Small Checks

| Dimension | Small check | What the evidence proves | Evidence boundary |
| --- | --- | --- | --- |


## Evidence and Boundaries

- Episode coverage: 0 episodes, 0 edited, 0 closed, 0 repaired-and-passed
- Model: agent-work-loop-v4
- Session selection: not observed; 0 sessions analyzed of 0 eligible sessions; not observed confidence
- Delivery grades observed: not observed
- Source gaps: not observed
- Learning comparison: Not observed; 0 declared intervention(s)
