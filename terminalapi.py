import requests, json

key = "API_KEY"
city = input("Enter city: ")

print("Fetching weather for", city)

url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=yes"

response = requests.get(url)
data = response.json()

formatted_data = json.dumps(data, indent=2)

print (formatted_data)
