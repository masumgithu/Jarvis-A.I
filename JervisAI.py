import speech_recognition as sr
import pyttsx3
import webbrowser
import openai

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        print("Listening...")
        audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}')
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None


if __name__ == '__main__':
    print('PyCharm')
    say('Hello, I am Jervis A.I.')
    while True:
        query = takeCommand()
        if query:
            sites = [
                ['youtube', 'https://www.youtube.com'],
                ['wikipedia', 'https://www.wikipedia.com'],
                ['google', 'https://www.google.com']
            ]
            for site in sites:
                if f'open {site[0]}' in query.lower():
                    say(f'Opening {site[0]} sir...')
                    webbrowser.open(site[1])
                    break

            if 'stop' in query.lower():
                say('Goodbye Sir!')
                break




