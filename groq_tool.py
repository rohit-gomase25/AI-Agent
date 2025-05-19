import os
import requests
from langchain.tools import Tool

def groq_query(query: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "GROQ API key not found in environment variables."

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
    "model": "llama3-70b-8192",
    "messages": [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": query}
    ],
    "temperature": 0.7,
    "max_tokens": 512
    }


    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error querying GROQ API: {e}"

groq_tool = Tool(
    name="groq_query",
    func=groq_query,
    description="Query the GROQ API with a natural language question.",
)
