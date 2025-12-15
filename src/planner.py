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

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
You are an agent planner.
Given the user request, produce a STRICT JSON object with:
- goal (string)
- steps (list of strings)
- proposed_tool (string)
- tool_input (string)

User request:
{user_input}
"""

    response = model.generate_content(prompt)

    # Gemini sometimes wraps JSON in text — be defensive
    text = response.text.strip()
    start = text.find("{")
    end = text.rfind("}") + 1
    json_text = text[start:end]

    return json.loads(json_text)
