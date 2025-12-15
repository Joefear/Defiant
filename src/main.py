from dotenv import load_dotenv
from planner import generate_plan


def main():
    # Load environment variables from .env
    load_dotenv()

    user_input = input("Enter a task for the agent: ")

    plan = generate_plan(user_input)

    print("\n--- Gemini Plan ---")
    for k, v in plan.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
