import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("TOGETHER_API_KEY")
openai.api_base = "https://api.together.xyz/v1"
MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"

def summarize_with_together(text: str) -> dict:
    def get_summary(level):
        prompt = f"Summarize the following YouTube transcript in {level} detail:\n\n{text}"
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

    return {
        "short": get_summary("very short"),
        "medium": get_summary("medium"),
        "detailed": get_summary("detailed")
    }
