import os
import uuid
import requests


def evaluate_with_guardrail(plan: dict, user_intent: str) -> dict:
    """
    Calls external Guardrail service.
    GuardrailRequest schema requires: request_id (str), intent (str), tool (object).

    Demo-safe behavior: fail CLOSED (deny) if Guardrail is configured but errors.
    """

    guardrail_url = os.getenv("GUARDRAIL_URL")

    # If Guardrail isn't configured, allow (so repo runs standalone).
    if not guardrail_url:
        return {
            "decision": "allow",
            "reason": "Guardrail not configured",
            "policy_id": "none",
            "risk_score": 0,
        }

    payload = {
        "request_id": str(uuid.uuid4()),
        "intent": user_intent,
        "tool": {
            "name": plan.get("proposed_tool"),
            "input": plan.get("tool_input"),
        },
    }

    try:
        r = requests.post(f"{guardrail_url}/v1/evaluate", json=payload, timeout=3)
        r.raise_for_status()
        return r.json()

    except Exception as e:
        # Fail CLOSED: if Guardrail is configured but unhealthy, deny.
        return {
            "decision": "deny",
            "reason": f"Guardrail error (fail-closed): {e}",
            "policy_id": "error",
            "risk_score": 90,
        }
