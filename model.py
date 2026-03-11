#loading Gemini Model through AI.Studio

import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

#Loading env
api_key = os.getenv("GEMINI_API_KEY")

#Initializing the Gemini client
client = genai.Client(api_key=api_key)

def generate_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
