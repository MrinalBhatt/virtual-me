import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
listener = sr.Recognizer()
# print(listener.listen())
engine.say('Namaste! I am virtual me')
engine.say('I can repeat what you say')

engine.runAndWait()
try:
    with sr.Microphone() as source:
        print('listening...')
        # print(listener)
        voice = listener.listen(source)
        # print(voice)
        command = listener.recognize_google(voice)
        engine.say(command)

        engine.runAndWait()
        print(command)
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
