from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage, SystemMessage

llm=ChatGroq(model="deepseek-r1-distill-llama-70b", api_key="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")

load_dotenv()

chat_history = []

#setting ann initial system Message
system_message = SystemMessage(content="you are an helpful ai assistant")
chat_history.append(system_message)

while True:
    query = input("You: ")
    if query.lower() == 'exit':
        break
    chat_history.append(HumanMessage(content=query.content))

    result = llm.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response.content))

    print(f"AI: {response}")

    print("----------------history----------------")
    print(chat_history)


