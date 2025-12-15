# Architecture Overview

Defiant Guardrail demonstrates an **agentic AI system with externalized policy enforcement**.
The agent plans actions using Gemini, but **cannot execute tools without Guardrail approval**.

---

## High-Level Flow

  - ┌────────────┐
  - │ User │
  - │ (CLI) │
  - └─────┬──────┘
  - │
  - ▼
  - ┌────────────┐
  - │ Agent │
  - │ (Gemini) │
  - │ Planner │
  - └─────┬──────┘
  - │ structured plan
  - ▼
  - ┌─────────────────────┐
  - │ Defiant Guardrail │
  - │ (FastAPI Service) │
  - │ /v1/evaluate │
  - └─────┬───────────────┘
  - │ allow / deny
  - ▼
  - ┌────────────┐
  - │ Tool / │
  - │ Action │
  - └────────────┘

-(All decisions are audit logged)


---

## Components

### 1. User Interface
- **CLI interface** (`src/main.py`)
- Used for clarity and fast iteration during the hackathon
- Accepts natural-language tasks from the user

---

### 2. Agent Core

#### Planner
- Implemented in `src/planner.py`
- Uses **Google Gemini (`gemini-2.5-flash`)**
- Converts user input into a structured plan:
  - goal
  - steps
  - proposed_tool
  - tool_input

#### Execution Controller
- Implemented in `src/main.py`
- Does **not** execute tools directly
- First sends planned action to Defiant Guardrail
- Enforces Guardrail allow/deny decision

There is **no inline prompt-based safety** — enforcement is external.

---

### 3. Guardrail Service (External)

- Implemented as a **standalone FastAPI service**
- Endpoint: `/v1/evaluate`
- Loads policy from `policy.yaml`
- Enforces:
  - Deny phrases (e.g. API keys, secrets)
  - Deny tools
  - Allow lists
- Returns:
  - decision (allow / deny)
  - policy_id
  - risk_score

This service is **model-agnostic** and reusable across agents.

---

### 4. Tools / APIs

- **Google Gemini API**
  - Used only for planning and reasoning
- **Defiant Guardrail API**
  - Used for real-time policy enforcement
- Tools are executed **only after Guardrail approval**

---

### 5. Observability & Audit Logging

- Every evaluation is logged with:
  - timestamp
  - request_id
  - intent
  - tool
  - decision
  - policy_id
  - risk_score
- Logs are queryable via:
  - `/logs/recent`

Judges can replay and inspect decisions deterministically.

---

## Design Principles

- **Fail-closed security**  
  If Guardrail is configured but unavailable, execution is denied.

- **Separation of concerns**  
  Planning ≠ execution ≠ policy enforcement.

- **Platform agnostic**  
  Guardrail can protect any agent, not just Gemini-based ones.

---

## Summary

This architecture demonstrates how agentic AI systems can remain flexible and powerful
while still being **governable, auditable, and policy-compliant**.
