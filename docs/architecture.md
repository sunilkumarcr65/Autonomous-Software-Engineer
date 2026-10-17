# Architecture

Issue → Orchestrator → Repository Explorer → Planner → Coder → Tester → Repair → Reviewer → PR.

State is explicit: CREATED → EXPLORING → PLANNING → CODING → TESTING → REVIEWING → PR_READY, with FAILED/BLOCKED/CANCELLED paths.

Advanced subsystems are planned behind interfaces: repository symbol/dependency/call graphs; persistent repository/task memory; permissioned sandbox execution; Git checkpoints and rollback; evaluation metrics; Redis-backed workers and WebSocket live events.

The key design principle is separation of orchestration from capabilities. An agent should request a capability through a controlled tool interface rather than directly owning shell, Git, database, and HTTP behavior.
