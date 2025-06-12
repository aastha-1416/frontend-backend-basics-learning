# Restricted key words list
restricted_keywords = [
    "black people", "ass", "bitch", "bastard", "africans",
    "cockhead", "homosexuality", "prostitution",
    "violation", "racial discrimination"
]

# Sentences list
sentenses = [
    "Well, I was born in the UK, and I speak African language.",
    "Are you BlaCK People?",
    "You a$$hole, don't call?",
    "Racial discrimination is bad.",
    "I was born prostitute in ancient Gaul, and escaped."
]

# Function to clean text
def clean_text(sentence):
    new_sentence = ""
    for char in sentence:
        if char.isalpha() or char == " ":
            new_sentence += char
        else:
            new_sentence += " "
    return new_sentence.lower().split()

# Function for keyword detection
def detect_keywords(stnc):
    word_list = clean_text(stnc)
    found = []

    for i in restricted_keywords:
        parts = i.split(" ")

        if len(parts) == 1:
            if parts in word_list:
                found.append(i)
        else:
            if parts[0] in word_list and parts[1] in word_list:
             found.append(i)

    return found


# Run loop to check all sentnces
for i in range(len(sentenses)):
    sentence = sentenses[i]
    result = detect_keywords(sentence)
    print("Sentenses:", i + 1)
    print(sentence)
    if result != []:
        print("Detected:", ", ".join(result), )
    else:
        print("All Clear")
