def Josh(person, k, index):
    if len(person) == 1:
        print("Survivor:", person[0])
        return

    index = (index + k) % len(person)
    person.pop(index)

    Josh(person, k, index)

n = 100         # Total people
k = 2           # Every k-th person will be killed
start = 5       # Starting from person number 5
k -= 1          # Adjust because killing starts at (k-1)
index = (start - 1) % n  # Convert starting person number to index

# Create the person list
person = list(range(1, n + 1))

Josh(person, k, index)
