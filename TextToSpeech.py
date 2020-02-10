import pyttsx3
text = 'How are you?'
Engine = pyttsx3.init()
Engine.setProperty('rate', 125)
Engine.say(text)
Engine.runAndWait()
# from gtts import gTTS
# from playsound import playsound
# import os
# userText = input('Enter the text: ')
# language = 'en'
# sound = gTTS(text = userText, lang = language, slow = False)
# sound.save('textToSound.mp3')
# playsound('textToSound.mp3')