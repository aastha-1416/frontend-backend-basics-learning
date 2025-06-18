from rapidfuzz import fuzz
import json

with open("mittal_patel.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

headline = data.get("headline")
occupation = data.get("occupation")

if headline and occupation:
    match_score = fuzz.ratio(occupation.lower(), headline.lower())
    print(f"Headline: {headline}")
    print(f"Occupation: {occupation}")
    print(f"Match Score: {match_score}% — {'Similar' if match_score >= 70 else 'Not Similar'}")
else:
    print("Headline or Occupation not available")
