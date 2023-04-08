import requests
sheety_api_url_post = "https://api.sheety.co/d48a0724d6289b81239e7d79266d44a9/flightDeals/users"
sheety_api_url_get = "https://api.sheety.co/d48a0724d6289b81239e7d79266d44a9/flightDeals/users"
data = requests.get(url = sheety_api_url_get)
print(data.json())
print("Welcome to Ritik Flight Club")
print("We find the best flight deals and email you.")
first_name =input("what is your first name? ")
last_name = input("What is your last Name? ")
Email = input("what is your email? ")
verify_email = input("Type your email again? ")
if Email!=verify_email:
    print("The email you have entered do not match.")
else:
    data = {}
    data['user'] = {'firstName':first_name,
            'lastName':last_name,
            'email':Email}
    response = requests.post(url=sheety_api_url_post,json=data)
    print("You are in the club")
