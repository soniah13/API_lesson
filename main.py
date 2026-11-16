import requests
import csv
import pandas as pd

endpoint = "https://jsonplaceholder.typicode.com/users"

response = requests.get(endpoint)
if response.status_code == 200:
    Users = response.json()
    # print(Users)


with open("users.txt", "a") as file:
    for user in Users[:5]:
        username = user["username"]
        email = user["email"]
        file.write(f"My name is {username} and my email is {email} \n")
print("Users saved to users.txt successfully")

with open("users.csv", "w") as csvfile:
    userWriter = csv.writer(csvfile)
    userWriter.writerow(["Name", "Email"])
    for user in Users[:5]:
        userWriter.writerow([user["name"], user["email"]])
print("users data stored in csv successfully")

data = []
for user in Users:
    data.append({
        "Username": user["username"],
        "Email": user["email"]
        })
df = pd.DataFrame(data)
df.to_excel("users.xlsx")
print("Data saved to excel successfully")
