from dotenv import load_dotenv
import os
from groq import Groq

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Prompt
prompt = """
Prioritize these developer tasks and explain why.

TODO: Add login validation
TODO: Add dark mode
FIXME: Optimize search algorithm
HACK: Temporary database connection

Return output in this format:

High Priority:
...

Medium Priority:
...

Low Priority:
...
"""

# Call model
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.3
)

# Print response
print(response.choices[0].message.content)