import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found in .env file"
    )

client = Groq(
    api_key=GROQ_API_KEY
)

#model="llama-3.3-70b-versatile"
model="llama-3.1-8b-instant"
def ask_llm(
    prompt: str,
    model: str = model,
    temperature: float = 0.3,
    max_tokens: int = 4000
) -> str:
    """
    Send prompt to Groq and return response text.
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert research assistant. "
                    "Provide clear, factual, structured answers."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_completion_tokens=max_tokens,
    )

    return response.choices[0].message.content