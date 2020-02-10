# Print tempearture.
import requests
try:
	location = input('Enter a city name: ')
	address = 'https://api.openweathermap.org/data/2.5/weather?q=' + location + '&units=metric&appid=60113b36f0a83502fe59ba9e512b76d4'
	data = requests.get(address)
	temp = eval(data.text)
	print('Temperature of ' + location + ' is ' + str(temp['main']['temp']) + '*c.')
except:
	print('Invalild city name!\n')