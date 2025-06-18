from rapidfuzz import fuzz
import json
import os
with open("mittal_patel.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

def shrink_summary(summary, limit=180):
    if len(summary) <= limit:
        return summary

    sliced = summary[:limit]

    for i in range(len(sliced) - 2, -1, -1):
        if sliced[i] in '.!?':
            if sliced[i + 1] == ' ':
                return sliced[:i + 1].strip()

    cut_at_space = sliced.rfind(' ')
    return sliced[:cut_at_space].strip()
