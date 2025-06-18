from rapidfuzz import fuzz
from datetime import datetime
import json
import os
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return None

def calculate_experience(experiences):
    total_days = 0
    current_role = None
    today = datetime.today()

    for exp in experiences:
        start = parse_date(exp.get("startDate"))
        end = parse_date(exp.get("endDate")) if not exp.get("isCurrent", False) else today

        if exp.get("isCurrent", False):
            current_role = exp.get("title", "Unknown")

        if start and end:
            total_days += (end - start).days

    years = total_days // 365
    months = (total_days % 365) // 30
    return current_role, years, months

with open("mittal_patel.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

experiences = data.get("experience", [])
if experiences:
    current, y, m = calculate_experience(experiences)
    print(f"Current Role: {current if current else 'Not Found'}")
    print(f"Total Experience: {y} years and {m} months")
else:
    print("Experience data not available")
