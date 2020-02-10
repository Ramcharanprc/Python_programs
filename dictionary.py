import  requests
import json
import pyttsx3
from playsound import playsound

app_id = '057c737e'
app_key = '7eaef497d58d5546402371088876d70f'
language = 'en'
print('Oxford Dictionaries.')
word = raw_input('Enter a word: ')
print
url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + word.lower()
meaning = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key}).json()
try: 
	playsound(meaning['results'][0]['lexicalEntries'][0]['pronunciations'][0]['audioFile'])
	for result in meaning['results'][0]['lexicalEntries'][0]['entries'][0]['senses']:
		print('Meaning:')
		print(result['definitions'][0])
		engine = pyttsx3.init()
		engine.setProperty('rate', 150)
		engine.say(result['definitions'][0])
		engine.runAndWait()
		print('Examples:')
		try:
			for example in result['examples']:
				print(example['text'])
		except KeyError:
			print('Examples not found.')
		print
except KeyError:
	print('No definitions found for this word.')
	