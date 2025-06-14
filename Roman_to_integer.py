def get_value(char):
    if char == 'I':
        return 1
    if char == 'V':
        return 5
    if char == 'X':
        return 10
    if char == 'L':
        return 50
    if char == 'C':
        return 100
    if char == 'D':
        return 500
    if char == 'M':
        return 1000
    return 0  

# Function to convert Roman numeral to integer
def roman_to_integer(s):
    total = 0
    i = 0

    while i < len(s):
        
        current = get_value(s[i])

       
        if i + 1 < len(s):
            next_val = get_value(s[i + 1])

            
            if current < next_val:
                total += (next_val - current)
                i += 2
            else:
                total += current
                i += 1
        else:
            total += current
            i += 1

    return total

# --- Test cases ---
print("Output 1:", roman_to_integer("III"))       
print("Output 2:", roman_to_integer("LVIII"))     
print("Output 3:", roman_to_integer("MCMXCIV"))   
