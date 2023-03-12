import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la"
token = ""
username = ""
graph_id = ""

# Creating a new user
def create_user():
    url = pixela_endpoint+'/v1/users'
    user_params ={
        "token":token,
        "username":username,
        "agreeTermsOfService":"yes",
        "notMinor":"yes"
    }
    response = requests.post(pixela_endpoint,json=user_params)
    response = response.json()
    return response

# Creating a graph
def create_graph():
    url = pixela_endpoint+f'/v1/users/{username}/graphs'
    headers = {"X-USER-TOKEN":token}
    graph_config ={
        "id":graph_id,
        "name":"coding",
        "unit":"minutes",
        "type":"int",
        "color":"sora",
    }
    response = requests.post(url,headers=headers,json=graph_config)
    response =response.json()
    return response

# get the graph
def get_graph():
    url = pixela_endpoint+f'/v1/users/{username}/graphs/{graph_id}/graph-def'
    headers = {"X-USER-TOKEN": token}
    response = requests.get(url,headers=headers)
    response =response.json()
    return response

# post a pixel
def post_pixel():
    url = pixela_endpoint+f'/v1/users/{username}/graphs/{graph_id}'
    headers = {"X-USER-TOKEN": token}
    date  = datetime.now().strftime("%Y%m%d")
    print(date)
    quantity = "50"
    graph_config ={
        "date":date,
        "quantity":quantity,
    }
    response = requests.post(url,headers=headers,json=graph_config)
    response =response.json()
    return response

def update_pixel():
    date = datetime.now().strftime("%Y%m%d")
    url = pixela_endpoint+f'/v1/users/{username}/graphs/{graph_id}/{date}'
    headers = {"X-USER-TOKEN": token}
    quantity = "70"
    graph_config = {
        "quantity": quantity,
    }
    response = requests.put(url, headers=headers, json=graph_config)
    response = response.json()
    return response


def delete_pixel():
    date = datetime.now().strftime("%Y%m%d")
    url = pixela_endpoint+f'/v1/users/{username}/graphs/{graph_id}/{date}'
    headers = {"X-USER-TOKEN": token}
    response = requests.delete(url, headers=headers)
    response = response.json()
    return response
    

print(delete_pixel())