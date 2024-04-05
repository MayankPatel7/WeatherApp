import requests

print("Welcome to weather app")
city = input("Enter the city name: ")

def get_request(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "YOUR API KEY"
    url = base_url+"appid="+api_key+"&q="+city+"&units=metric"
    data = requests.get(url).json()

    name = data['name']
    coord = {"Longitudes" : data['coord']['lon'], "Latitudes" : data['coord']['lat']}
    temp = str(data['main']['temp'])+"° C"
    desc = data['weather'][0]['description']
    wind = str(data['wind']['speed'])+"kmph"

    print("City name:", name)
    print("Coordiates:", coord)
    print("Temperature:", temp)
    print("Description:", desc)
    print("Wind Speed:", wind)

get_request(city)
