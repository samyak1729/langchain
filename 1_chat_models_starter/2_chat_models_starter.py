from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)


messages = [
    SystemMessage("You are a marketing genius"),
    HumanMessage("tip on promoting a wearable device for parkinsons disease early detection")

]

result = llm.invoke(messages)

print(result.content)
