import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def calculate(a: int, b: int) -> str:
    """Perform for basic arithmeric calculation."""
    return f"The result of adding {a} and {b} is {a + b}."



def main():
    model = genai.GenerativeModel("gemini-1.5-flash")

    print("Welcome to the React Agent! Type 'exit' to quit.")
    print("You can ask me perform calculation or chat with me.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the React Agent. Goodbye!")
            break
        
         # Simple tool call detection
        if "calculate" in user_input.lower():
            try:
                parts = [int(x) for x in user_input.split() if x.isdigit()]
                if len(parts) >= 2:
                    result = calculate(parts[0], parts[1])
                    print(f"Agent: {result}")
                    continue
            except Exception as e:
                print(f"Agent: Sorry, error in calculation → {e}")
                continue

        # Otherwise, use Gemini for free-form chat
        response = model.generate_content(user_input)
        print("Agent:", response.text)

if __name__ == "__main__":
    main()