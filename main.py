from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field
from regex import search


load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """ Schema for a source used by the agent. """
    url: str = Field(description="The url of the source")

class AgentResponse(BaseModel):
    """ Schema for the result returned by the agent with answer and sources. """
    answer: str = Field(description="The answer to the question")
    sources: List[Source] = Field(default_factory=list, description="The sources used to answer the question")
    

search = TavilySearch()


llm= ChatOpenAI()
tools = [search]
# agent = create_agent(model=llm, tools=tools)
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job posting for an ai engineer using langchain in Austin Area in linkedin and list all the details of the job posting including the company name, job title, location, and a brief description of the job.")})
    print(f"Agent result: {result}")

if __name__ == "__main__":
    main()
