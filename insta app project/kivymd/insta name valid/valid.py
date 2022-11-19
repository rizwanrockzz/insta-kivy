import requests

username = input("Enter the username : ")
response = requests.get("https://instagram.com/" + username + "/")
if response.status_code == 404 :
    print("The username doesnot exists")
else:
    print("The username exists")