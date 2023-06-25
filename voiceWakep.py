# Speech to text library
import speech_recognition as sr
# Text to Speech library
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the properties (optional)
engine.setProperty('volume', 0.8)  # Set volume (0.0 to 1.0)
engine.setProperty('rate', 150)    # Set speech rate (words per minute)
engine.setProperty('voice', 'en-in')  # Set voice (specific voice ID or use the default)

# Use the default microphone as the audio source and taking input form user
with sr.Microphone() as source:
    print("Listening...")
    userInput = r.listen(source)
    keyword = r.recognize_google(userInput).title()

    # cases for keyword deeksha
    if keyword == 'Diksha':
        wakeUpWord = 'Diksha'
    elif keyword == 'Deeksha':
        wakeUpWord = 'Diksha'

    if keyword == 'Diksha':
        text = r.recognize_google(userInput)
        print(text)
        engine.say("Yes,Baby.")
        engine.runAndWait()
    else:
        text = r.recognize_google(userInput)
        print(text)
        engine.say("I didn't get that.")
        engine.runAndWait()
    # making voice activation function
    # try:
    #     keyword = r.recognize_google(userInput)
    # When User input is not being understood    
    # except sr.UnknownValueError:
    #     engine.say("I didn't get that , Please try again")
    #     engine.runAndWait()
    # When service in not available    
    # except sr.RequestError:
    #     engine.say('PLease check your internet connection and try again')
    #     engine.runAndWait()  


# Convert speech to text
# try:
#     text = r.recognize_google(userInput)
#     engine.say(text)
#     engine.runAndWait()
# except sr.UnknownValueError:
#     print("Sorry, I couldn't understand what you said.")
# except sr.RequestError:
#     print("Sorry, speech recognition service is currently unavailable.")
