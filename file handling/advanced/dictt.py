import json

# ---------- Write ----------
user = {
    "name": "Srinithi",
    "age": 22,
    "city": "Bengaluru"
}

fp = open("user.json", "w")
json.dump(user, fp, indent=4)
fp.close()

print("User data written to user.json")

# ---------- Read ----------
fp = open("user.json", "r")
data = json.load(fp)
fp.close()

print("\nReading from file:")
for key, value in data.items():
    print(key, ":", value)
