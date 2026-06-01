from groq import Groq
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

def llm_response(content):
    prompt = f"""You are a highly qualified Literary Professor specializing in summarizing \
    large-scale texts and documents given by students.

    Document Context:
    {content}

    Summarize the document in 100 words, covering all key topics without missing any point."""

    client=Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": content
        }
    ]
)
    print(response.choices[0].message.content)