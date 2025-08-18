from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculate(a: int, b: int) -> str:
    """Perform for basic arithmeric calculation."""
    return f"The result of adding {a} and {b} is {a + b}."



def main():
    model = ChatOpenAI(temperature=0)

    tools = [calculate]

    agent_executor = create_react_agent(
        model=model,
        tools=tools,)
    
    print("Welcome to the React Agent! Type 'exit' to quit.")
    print("You can ask me perform calculation or chat with me.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the React Agent. Goodbye!")
            break
        
        print("\nAgent: ", end="")
        for chunk in agent_executor.stream({"input": [HumanMessage(content=user_input)]}):
            if "agent" in chunk and "message" in chunk["agent"]:
                for message in chunk["agent"]["message"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()