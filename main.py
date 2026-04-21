from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

search = TavilySearch()


llm= ChatOpenAI()
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job posting for an ai engineer using langchain in Austin Area in linkedin and list all the details of the job posting including the company name, job title, location, and a brief description of the job.")})
    print(f"Agent result: {result}")

if __name__ == "__main__":
    main()
