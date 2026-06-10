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

with open("sample.cpp", "r") as file:
    lines = file.readlines()

for line_no, line in enumerate(lines, start=1):
    for keyword in keywords:
        if keyword in line:
            print(f"Line {line_no}: {line.strip()}")