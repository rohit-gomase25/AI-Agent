from dotenv import load_dotenv
from pydantic import BaseModel
from groq_tool import groq_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

def main():
    query = input("How can I help you? ")
    try:
        raw_response = groq_tool.func(query)
        print("Response from GROQ API:")
        print(raw_response)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
