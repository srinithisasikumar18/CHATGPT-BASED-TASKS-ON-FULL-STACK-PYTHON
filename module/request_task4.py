import requests

res=requests.get("https://jsonplaceholder.typicode.com/users")

users=res.json()
for user in users:
    print(user['name'],"->",user['address']['city'])
