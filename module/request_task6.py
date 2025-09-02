import requests

res=requests.get("https://jsonplaceholder.typicode.com/users")
user_city=(input("enter the user city"))
users=res.json()
for user in users:
    if user['address']['city']==user_city:
        print(user['name'],"->",user['address']['city'])
