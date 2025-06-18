#read json

import json

with open('sample.json', 'r') as f:
	data = json.load(f)

print(data)



#Convert from JSON to Python:
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)# parse x:
# the result is a Python dictionary:
print(y["age"])



#Convert from Python to JSON:
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)