from dotenv import load_dotenv
import os
import requests
import base64
import json
from groq import Groq

load_dotenv()

GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

PROJECT_ID = 83028931

KEYWORDS = [
    "TODO",
    "FIXME",
    "HACK",
    "BUG",
    "REFACTOR"
]

headers = {
    "PRIVATE-TOKEN": GITLAB_TOKEN
}

# -----------------------------------
# STEP 1: Get all files in repository
# -----------------------------------

tree_url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/repository/tree"

files_response = requests.get(tree_url, headers=headers)

files = files_response.json()

tasks = []

# -----------------------------------
# STEP 2: Scan every .cpp file
# -----------------------------------

for file in files:

    if not file["name"].endswith(".cpp"):
        continue

    filename = file["name"]

    print(f"\nScanning {filename}...")

    file_url = f"https://gitlab.com/api/v4/projects/{PROJECT_ID}/repository/files/{filename}?ref=main"

    response = requests.get(file_url, headers=headers)

    data = response.json()

    content = base64.b64decode(
        data["content"]
    ).decode("utf-8")

    for line_no, line in enumerate(content.splitlines(), start=1):

        for keyword in KEYWORDS:

            if keyword in line:

                task = {
                    "file": filename,
                    "line": line_no,
                    "type": keyword,
                    "task": line.strip()
                }

                tasks.append(task)

# -----------------------------------
# STEP 3: Save tasks.json
# -----------------------------------

with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

# -----------------------------------
# STEP 4: Print Tasks
# -----------------------------------

print("\nDetected Tasks:\n")

for task in tasks:
    print(
        f"{task['file']} | Line {task['line']} | {task['task']}"
    )

# -----------------------------------
# STEP 5: Statistics
# -----------------------------------

todo_count = sum(
    1 for task in tasks if task["type"] == "TODO"
)

fixme_count = sum(
    1 for task in tasks if task["type"] == "FIXME"
)

hack_count = sum(
    1 for task in tasks if task["type"] == "HACK"
)

print("\nStatistics:\n")

print(f"Total Tasks: {len(tasks)}")
print(f"TODOs: {todo_count}")
print(f"FIXMEs: {fixme_count}")
print(f"HACKs: {hack_count}")

# -----------------------------------
# STEP 6: Send to Groq
# -----------------------------------

client = Groq(
    api_key=GROQ_API_KEY
)

task_list = "\n".join(
    task["task"] for task in tasks
)

prompt = f"""
You are a senior software engineer.

Prioritize these tasks:

{task_list}

Classify them into:
1. High Priority
2. Medium Priority
3. Low Priority

Explain why.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

analysis = response.choices[0].message.content

# -----------------------------------
# STEP 7: Save analysis
# -----------------------------------

with open(
    "analysis.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(analysis)

print("\nAI Analysis:\n")
print(analysis)