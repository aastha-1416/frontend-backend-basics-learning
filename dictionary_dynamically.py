input = {
    "Apps - Health and Fitness Apps": 50,
    "Apps - Lifestyle Apps": 20,
    "Arts and Entertainment - Experiences and Events - Concerts": 45,
    "Arts and Entertainment - Experiences and Events - Theatre and Musicals": 75,
    "Consumer Packaged Goods - Edible - Beverages - Coffee & Tea - Coffee Filters": 80,
    "Consumer Packaged Goods - Edible - Beverages - Coffee & Tea - Tea - Bags/loose": 99,
    "Consumer Packaged Goods - Non-edible - Household Appliances - Air Conditioners": 95,
    "Consumer Packaged Goods - Non-edible - Household Appliances - Air Purifiers": 77,
    "Consumer Packaged Goods - Non-edible - Household Appliances - Blenders": 67,
    "Consumer Packaged Goods - Non-edible - Beauty - Hair Care - Home Permanent/Relaxer Kits": 85,
    "Consumer Packaged Goods - Non-edible - Beauty - Personal Cleansing - Bath Products": 45,
    "Consumer Packaged Goods - Non-edible - Beauty - Personal Cleansing - Bath/Body Scrubbers/Massagers": 35,
    "Consumer Packaged Goods - Non-edible - General Merchandise - Miscellaneous General Merch - Firelog/Firestarter/Firewood": 75,
    "Consumer Packaged Goods - Non-edible - Beauty - Hair Care - Hair Conditioner": 61
}


output = {}

# Function to manually split a string by " - "
def manual_split(text):
    parts = []
    temp = ""
    i = 0
    while i < len(text):
        if i + 2 < len(text) and text[i] == ' ' and text[i+1] == '-' and text[i+2] == ' ':
            parts.append(temp)
            temp = ""
            i += 3  # skip ' - '
        else:
            temp += text[i]
            i += 1
    parts.append(temp) 
    return parts

# Manually process each key and insert value
for full_key in input:
    keys = manual_split(full_key)
    value = input[full_key]

    current_dict = output
    index = 0

    while index < len(keys):
        key = keys[index]

        if index == len(keys) - 1:
          
            current_dict[key] = value
        else:
           
            found = False
            for existing_key in current_dict:
                if existing_key == key:
                    found = True
                    break
            if not found:
                current_dict[key] = {}
            current_dict = current_dict[key]
        index += 1


print(output) 