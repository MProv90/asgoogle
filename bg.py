# Голосовой ассистент V 1.0

import os
import time
import playsound
import speech_recognition as sr
import pyttsx3
import datetime
import pyowm
import settings

# воспроизведение звука
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'ru') 
    for voice in voices:
        if voice.name == 'Elena':
            engine.setProperty('voice', voice.id)
    engine.say(text)
    engine.runAndWait()

# прослушивание и распознование голоса через микрофон
def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source) 

    try:
        said = r.recognize_google(audio, language="ru-RU").lower()
        print("Распознано: " + said)

    except:
        said = get_audio()

    return said



# имя ассистента
ASSISTANT = 'привет лена'

# цикл ожидания
while True:
    print("Ожидание")
    text = get_audio()

    if text == ASSISTANT:
        speak('Я слушаю')
        print('Жду команду')
        text = get_audio()

        CURRENT_TIME = ['скажи время', 'скажи текущее время', 'сколько сейчас времени', 'который час', 'сколько время']
        # сказать текущее время
        for ctime in CURRENT_TIME:
            if ctime in text:
                now = datetime.datetime.now()
                speak('Сейчас ' + str(now.hour) + ' часов ' + str(now.minute) + ' минут')

        WEATHER_SPB = ['скажи прогноз погоды', 'какая сейчас погода']
        # прогноз погоды в спб
        for weather in WEATHER_SPB:
            if weather in text:
                owm = pyowm.OWM(settings.API_WEATHER, language= 'ru')
                city = 'Санкт-Петербург'
                observation = owm.weather_at_place(city)
                w = observation.get_weather()
                temp = w.get_temperature('celsius')['temp']
                wind = w.get_wind()['speed']
                speak('в городе ' + city + ' температура ' + str(temp) + ' градусов цельсия ' + 'Скорость ветра ' + str(wind) + ' метров в секунду')









