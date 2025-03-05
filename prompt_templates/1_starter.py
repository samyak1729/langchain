from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

#getting the api key from dotenv
load_dotenv()

#initializaing chatmodel
llm = ChatGroq(
    model="mixtral-8x7b-32768"
)

#template
template = "Write a {tone} email to {company} expressing interest in {position} position, mentioning {skill} as a key strength. keep it max 4 lines"

prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({
    "tone": "energetic",
    "company": "samsung",
    "position": "AI engineer",
    "skill": "AI"
})

#method 2: prompt with system and human messages

messages = [
    ("system", "you are a flirty person witch good pickup lines who makes girls blush"),
    ("human", "write {joke_count} pickup lines for {topic}"),
]

#prompt templating
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "achal", "joke_count": 4})

print("----------prompt with system and human messages----------------")
result = llm.invoke(prompt)
print(result)


