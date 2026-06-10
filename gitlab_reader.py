from dotenv import load_dotenv
import os
import requests
import base64

load_dotenv()

TOKEN = os.getenv("GITLAB_TOKEN")

PROJECT_ID = 83028931

keywords = [
    "TODO",
    "FIXME",
    "HACK",
    "BUG",
    "REFACTOR",
    "OPTIMIZE",
    "REVIEW",
    "WORKAROUND"
]

headers = {
    "PRIVATE-TOKEN": TOKEN
}

url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/repository/files/main.cpp?ref=main"

response = requests.get(url, headers=headers)

data = response.json()

content = base64.b64decode(data["content"]).decode("utf-8")

lines = content.splitlines()

for line_no, line in enumerate(lines, start=1):
    for keyword in keywords:
        if keyword in line:
            print(f"Line {line_no}: {line.strip()}")