import requests, json

key = "API_KEY"
city = input("Enter city: ")

print("Fetching weather for", city)

url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=yes"

response = requests.get(url)
data = response.json()

keys = ['location', 'current']

city = data.get("location", {}).get("name", "Unknown")
country = data.get("location", {}).get("country", "Unknown")
temp = data.get("current", {}).get("temp_c", "Unknown")

info = [data.get(key) for key in keys]

print("City: ", city)
print("Country: ", country)
print("Current Temperature (Celsius): ", temp)

ask_user = input("\nWant full data?: ")

if ask_user.lower() in ['yes', 'y']:
    print(json.dumps(data, indent=4))
else:
    print("Invalid input!")
