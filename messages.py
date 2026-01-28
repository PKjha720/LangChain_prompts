from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()
model=ChatGroq(model="llama-3.1-8b-instant")
messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='tell me about langChain')
]
result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)