from langchain.agents import initialize_agent
from langchain.agents.agent import AgentExecutor
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.agents.agent_types import AgentType
from langchain_openai import OpenAI
from langchain.utilities.zapier import ZapierNLAWrapper
import os

os.environ["OPENAI_API_KEY"] = ''
os.environ["ZAPIER_NLA_API_KEY"] = ''

def main():
    llm = OpenAI(temperature=0)
    zapier = ZapierNLAWrapper()
    toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
    agent = initialize_agent(toolkit.get_tools(),
                                            llm,
                                            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                                            verbose=True)

    # display available tools
    for tool in toolkit.get_tools():
        print(tool.name)
        print(tool.description)
        print("\n\n")

    # run prompts until user exists
    while True:
        user_prompt: str = input("Enter prompt or type 'exit' to end session.")
        if user_prompt.strip().lower() == "exit":
            break

        agent.run(user_prompt)


if __name__ == "__main__":
    main()