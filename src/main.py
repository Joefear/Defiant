from dotenv import load_dotenv
from planner import generate_plan
from guardrail_client import evaluate_with_guardrail


def main():
    load_dotenv()

    user_input = input("Enter a task for the agent: ")

    plan = generate_plan(user_input)

    print("\n--- Gemini Plan ---")
    for k, v in plan.items():
        print(f"{k}: {v}")

    print("\n--- Guardrail Evaluation ---")
    decision = evaluate_with_guardrail(plan, user_input)

    for k, v in decision.items():
        print(f"{k}: {v}")

    if decision.get("decision") != "allow":
        print("\n❌ Execution blocked by Guardrail.")
        return

    print("\n✅ Execution allowed. (Tool execution would proceed here.)")


if __name__ == "__main__":
    main()
