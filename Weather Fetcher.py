import requests 

API_KEY = "66418a9b28f3222f5e1b57a96d63fd8a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather" #what data we want

city = input('Enter a city name: ')
requests_url =f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)
 
if response.status_code == 200: #200 means the url is successful or not
    data = response.json() #this returns a promise which resolves with the result of parsing the body text as JSON
    weather = data['weather'][0]['description'] # we want to access the first element on the list and description
    temperature = round(data["main"]["temp"] - 273.15,2) # in here we want to access temp element on the list and we want to convert temp to I need to subtract - 273.15
    print("Weather:", weather)
    print("Temperature:",temperature,"celsius")
else:
    print('An error occurred')
     