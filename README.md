# Defiant Guardrail — Agentic AI Security Middleware (Gemini Hackathon)

Defiant Guardrail is a **policy-driven AI security layer** that protects agentic systems from
credential leakage, unsafe tool use, and policy violations — without modifying the model itself.

This repository contains:
- A runnable **Guardrail service** (FastAPI)
- A **Gemini-powered agent demo** that calls Guardrail before executing tasks
- A complete **hackathon demo flow** with audit logs and deny enforcement

---

## 🚨 The Problem

Agentic AI systems frequently:
- Leak API keys and credentials
- Execute unsafe tools
- Violate enterprise or compliance rules
- Behave inconsistently across apps (CLI, web, API, bots)

Traditional solutions require custom middleware per app.

**Defiant Guardrail solves this with a single policy-based service** any agent can call.

---

## 🧠 What Guardrail Does

- Evaluates agent intent **before execution**
- Enforces YAML-based policies
- Blocks disallowed phrases, tools, and actions
- Produces **audit logs** for every decision
- Works with Gemini or any LLM

---

## 🏗️ Architecture (High-Level)

    User Input
       ↓
    Agent (Gemini)
       ↓
    Guardrail /v1/evaluate
       ↓
    Allow → Execute Tool
    Deny  → Block + Log


Guardrail runs as a standalone service and can protect:
- CLI agents
- Web apps
- APIs
- MCP-compatible tools (future extension)

