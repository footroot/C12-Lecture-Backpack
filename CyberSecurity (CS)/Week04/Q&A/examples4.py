import json

with open('files\\example.json') as file:
    data = json.load(file)

print(data)

for user in data['users']:
    print(f"ID: {user['id']}\nName: {user['name']}\nEmail: {user['email']}")