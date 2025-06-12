text = "apple banana"
vowels = "aeiou"
count = {}
for char in text.lower():
    if char in vowels:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
print(count)
