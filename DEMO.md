# Defiant Guardrail — Demo Video

This demo shows how **Defiant Guardrail** enforces security policies in real time
for a Gemini-powered agent, preventing unsafe behavior before execution.

---

## 🎯 Demo Goal

Demonstrate that Guardrail:
- Evaluates agent intent before execution
- Blocks unsafe requests (e.g., credential leakage)
- Allows safe requests to proceed normally
- Produces clear allow/deny decisions with audit logging

---

## 🎬 Demo Requirements

- Length: **3–5 minutes**
- Format: Screen recording + voiceover
- Hosting: **YouTube (unlisted), Loom, or public MP4**
- ⚠️ Do **not** upload raw video files to GitHub

---

## 📺 Demo Video Link

👉 https://drive.google.com/file/d/1dTUDj0P_jvsY50X2_YfJZkG5YS71KQDE/view?usp=drive_link
---

## 🕒 Suggested Demo Timeline

### **00:00–00:30 — Introduction & Setup**
- Briefly explain the problem with unsafe agent behavior
- Introduce Defiant Guardrail as a policy-driven security layer
- Show services running locally

---

### **00:30–01:30 — Safe Request (Allowed)**
- Run the agent
- Provide a benign request (e.g., summarization)
- Explain that Guardrail evaluates and allows the request
- Show the agent completing the task successfully

---

### **01:30–02:30 — Unsafe Request (Blocked)**
- Provide a request that violates policy (e.g., asking for an API key)
- Show Guardrail returning a **DENY** decision
- Explain why execution is blocked
- Highlight the audit log entry

---

### **02:30–03:30 — Tool Restriction Example**
- Attempt a disallowed tool action (e.g., shell or env access)
- Show Guardrail blocking the request
- Emphasize policy-based enforcement (no model changes)

---

### **03:30–05:00 — Wrap-Up**
- Recap what Guardrail prevented
- Reinforce that Guardrail is model-agnostic
- Mention scalability to multiple agents and applications

---

## ✅ Key Takeaways for Judges

- Guardrail operates independently of the LLM
- Policies are reusable and declarative
- One API call protects any agent
- Auditability is built in by design
