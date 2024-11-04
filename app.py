
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage,SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY=os.getenv('TAVILY_API_KEY')
model = ChatGroq(model="llama3-8b-8192")

# memory = MemorySaver()
search = TavilySearchResults(max_results=2)
tools = [search]

system_message = SystemMessage(
    content="Only use tools for questions requiring specific information or data lookup. "
            "For simple introductions or casual conversation, respond directly without any tool."
)
memory = MemorySaver()
agent_executor = create_react_agent(model, tools,checkpointer=memory)
config = {"configurable": {"thread_id": "abc123"}}

for chunk in agent_executor.stream(
    {"messages": [system_message,HumanMessage(content="What is the whether in SF?")]}, config
):
    print(chunk)
    print("----")

