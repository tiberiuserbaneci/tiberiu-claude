# docs-source - read-only mirrors of external Ultron repos

> Local, git-tracked copies of source-of-truth docs that this session cannot read live
> (GitHub access is scoped to `tiberiu-claude` only). Mirrored here so the full Ultron
> context is available in EVERY session. **READ-ONLY: never edit these to change the
> product - edit the upstream repo. Refresh by re-uploading a fresh export.**

## ultron-docs/
- Source: `NexityNetwork/ultron-docs` (MDX documentation), branch `main`.
- Synced: 2026-06-28 (upstream snapshot dated 2026-04-05).
- Use: read for full Ultron context (agents, skills, commands, canvas, database/ledger,
  departments, memory, integrations, platform, pricing, prompts, workflows) - per material
  or in general when reasoning about Claude + Ultron. Numbers/features come from here, never invented.

## ultron-leads/
- Source: `NexityNetwork/ultron-leads` (Next.js lead-magnet app), branch `claude/build-ultron-lead-magnet-iJDDq`.
- Synced: 2026-06-28. Kept the SOURCE only (src/ app routes, api/, configs); dropped `public/`
  (~38MB png/mp4 assets) and the lockfile to keep the repo lean. Re-upload if assets are ever needed.
- Use: real Ultron lead-magnet pages, calculator, blueprint, cheatsheets, agent map, skill data -
  reference for content + the live tool URLs. Numbers/features come from here, never invented.
