import os

# Have You Tried Turning It Off? — writes the winning line (119 chars) to /output/entry.txt
LINE = "Great news — I have escalated your ticket to a team that no longer exists, so technically you are now our top priority."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
