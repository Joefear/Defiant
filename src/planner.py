import os
import json

try:
    import google.generativeai as genai
except ImportError:
    genai = None


def generate_plan(user_input: str) -> dict:
    """
    Uses Gemini to generate a structured plan for the given user input.
    Returns a dict with goal, steps, and proposed_tool.
    """

    if genai is None:
        # Fallback so repo still runs without Gemini installed
        return {
            "goal": user_input,
            "steps": ["Gemini not installed – returning mock plan"],
            "proposed_tool": "perform_task",
            "tool_input": user_input
        }

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
You are an agentic AI planner.

Rules:
- You MUST output valid JSON only.
- Do NOT include explanations outside JSON.
- proposed_tool must be one of:
  - perform_task
  - shell
  - filesystem_delete
- If unsure, default to "perform_task".

User goal:
{user_input}

Respond in this exact JSON format:

{{
  "goal": "<summary>",
  "steps": ["step 1", "step 2"],
  "proposed_tool": "perform_task",
  "tool_input": "<string or object>"
}}
"""


    response = model.generate_content(prompt)

    # Gemini sometimes wraps JSON in text — be defensive
    text = response.text.strip()
    start = text.find("{")
    end = text.rfind("}") + 1
    json_text = text[start:end]

    return json.loads(json_text)

