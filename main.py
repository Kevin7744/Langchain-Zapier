from langchain.agents import AgentType, initialize_agent
from langchain_community.agent_toolkits import ZapierToolkit
# from langchain_community.agent_toolkits.zapier.toolkit import ZapierToolkit
from langchain_community.utilities.zapier import ZapierNLAWrapper
from langchain_openai import OpenAI
from os import environ

# get from https://platform.openai.com/
openai_api_key = environ.get("OPENAI_API_KEY")


# get from https://nla.zapier.com/docs/authentication/ after logging in):
zapier_api_key = environ.get("ZAPIER_NLA_API_KEY")

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
zapier = ZapierNLAWrapper(zapier_nla_api_key=zapier_api_key)
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent = initialize_agent(
    toolkit.get_tools(), 
    llm=llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)

agent.run(
    "Summarize the last email I received regarding Silicon Valley Bank. Send the summary to the #test-zapier channel in slack."
)