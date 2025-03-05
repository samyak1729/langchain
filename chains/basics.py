from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="mixtral-8x7b-32768",
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a facts expert who knows facts on {topic}"),
        ("human", "Tell me {fact_count} facts")
    ]
)

#create combines chain using Lanchain expression langauge (LECL)
chain = prompt_template | model | 

#run the chain
result = chain.invoke({"animal": "cat", "fact_count": 2})

#print result
print(result)
