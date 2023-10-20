import requests

url = 'http://localhost:5000/predict'
data = {
    "Age": [32],
    "Gender": ['Male'],
    "Location": ["Houston"],
    "Subscription_Length_Months": [12],
    "Monthly_Bill": [48.76],
    "Total_Usage_GB": [172],
}

response = requests.post(url, json=data)
print(response.json())