from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN = os.getenv("GITLAB_TOKEN")
PROJECT_ID = 83028931

headers = {
    "PRIVATE-TOKEN": TOKEN
}

url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/issues"

data = {
    "title": "Test Issue Created By Second Brain Agent",
    "description": "This issue was created automatically by the agent."
}

response = requests.post(
    url,
    headers=headers,
    data=data
)

print(response.status_code)
print(response.json())