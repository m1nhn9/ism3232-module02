# hello_ism3232.py
# Author: Minh Tan Nguyen
# --- What happened when I ran this script? ---
# 1. The shell found python3 at: /Users/hoo/ism3232/module02_zsh/.venv/bin/python3
# 2. Python read the file from top to bottom: True
# 3. The f-string evaluated {weekly_hours} to: 6
# 4. The output appeared in the terminal.

print("Hello, ISM3232!")

course_name = "Business Application Development"
credit_hours = 3
weekly_hours = credit_hours * 2

print(f"Course: {course_name}")
print(f"Expected weekly hours: {weekly_hours}")
print("Environment verified. Week 1 complete.")
