import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "grades": [90, 85, 92]
}

# Serialize to a JSON string with indentation
json_string_formatted = json.dumps(data, indent=4)
print(json_string_formatted)

# Serialize to a compact JSON string
json_string_compact = json.dump(data,'users.json')
print(json_string_compact)