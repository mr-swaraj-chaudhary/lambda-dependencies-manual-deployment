import requests

def lambda_handler(event, context):   
    response = requests.get("https://www.google.com/")
    return response.text 