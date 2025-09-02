import requests

res=requests.get("https://jsonplaceholder.typicode.com/users")
user_id=int(input("enter the user id"))
users=res.json()
for user in users:
    if user['id']==user_id:
        print(user['name'],"->",user['email'])
    else:
        print("User doesn't exist")