import pyttsx3
import datetime
import speech_recognition as sr
import json
import pyaudio

bedR = 0
kitch = 1
garage = 2

tempVals = [20, 21, 22]
co2Vals = [1200, 1500, 1800]
humVals = [60, 80, 95]
rooms = ['bedroom', 'kitchen', 'garage']
events = ['temperature', 'CO2', 'humidity']


#Parse Func for my data
def parseThis(x):
    with open('units.json', 'r') as f:
        home_unit = json.load(f)

    for value in home_unit:

        answer = print(value[x])

    return answer


#Listener...1
listener = sr.Recognizer()

#speak function to enable our assistant to talk
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#2
#Creating enviroment for my assistnt
engine = pyttsx3.init()

#sets voice to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#dynamic talk function. pass in whatever param you want
def talk(text):
    engine.say(text)
    engine.runAndWait()

#1
#take the command we speak
def take_command():
    try:
        #use microphone as source
        with sr.Microphone() as source:
            print("Processing...")
            #listen to your voice as the source
            voice = listener.listen(source)
            #pass the audio to google and google returns text
            command = listener.recognize_google(voice)
            command = command.lower()
            #only prints what you say if electron is said

            if 'electron' in command:
                #this removes 'electron from the string while having it as a wake word still
                #command = command.replace('electron', '')
                print(command)
               # talk(command) #will repeat back to you what you said
    except:
        pass
    return command

take_command()

def bedroom_unit():
    command = take_command()
    #command = "electron what is the tempeature in the bedroom"
    #electron must be said for this to speak
    if 'electron' in command:
        #bedroom must be spoken for this to activate
        if 'kitchen' in command:
            #if the user asks for any of theses values they will be spoken
            if 'temperature' in command:
                        talk(tempVals[bedR] + 'degrees')
                        #talk('degrees')

            elif 'c. o. two' in command:
                        talk(co2Vals[bedR])
                        talk('ppm')

            elif 'humidity' in command:
                        talk(humVals[bedR])
                        talk('percent')
    #message printed to suggest why it didnt work
    else:
        command2 = "why did you not tell me"
       #command2 = take_command()
        if 'why' and 'not' in command2:
          talk("I am not telling you, because you never said my name!")

bedroom_unit()


def kitchen_unit():
    #command = take_command()
    command = "electron what is the tempeature in the bedroom"
    #electron must be said for this to speak
    if 'electron' in command:
        #bedroom must be spoken for this to activate
        if 'kitchen' in command:
            #if the user asks for any of theses values they will be spoken
            if 'temperature' in command:
                        talk(tempVals[kitch])
                        talk('degrees')

            elif 'c. o. two' in command:
                        talk(co2Vals[kitch])
                        talk('ppm')

            elif 'humidity' in command:
                        talk(humVals[kitch])
                        talk('percent')
    #message printed to suggest why it didnt work
    else:
        command2 = "why did you not tell me"
       #command2 = take_command()
        if 'why' and 'not' in command2:
          talk("I am not telling you, because you never said my name!")

#kitchen_unit()


def garage_unit():
    #command = take_command()
    command = "electron what is the tempeature in the bedroom"
    #electron must be said for this to speak
    if 'electron' in command:
        #bedroom must be spoken for this to activate
        if 'kitchen' in command:
            #if the user asks for any of theses values they will be spoken
            if 'temperature' in command:
                        talk(tempVals[garage])
                        talk('degrees')

            elif 'c. o. two' in command:
                        talk(co2Vals[garage])
                        talk('ppm')

            elif 'humidity' in command:
                        talk(humVals[garage])
                        talk('percent')
    #message printed to suggest why it didnt work
    else:
        command2 = "why did you not tell me"
       #command2 = take_command()
        if 'why' and 'not' in command2:
          talk("I am not telling you, because you never said my name!")

garage_unit()

#def run_alexa():
  #  command = take_command()


#speak("hello this is Electron the Ei home assistant")


#Function to speak current time
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

#time()


#Func to speak current date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)

#date()


#Func to greet our user with time sensitivty
def greet_me():

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning user!")
    elif hour >= 12 and hour <18:
        speak("Good evening user!")
    else:
        speak("Good night user!")

    speak("How can I help you?")

#greet_me()


#speech recognition function...
def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Listening...")
        query = r.recognize_google(audio, language="en")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again?")

        return "Null"
    return query

#get_command()


# If a temperature hits a certain level speak "Your temperature has hit an unsafe level"
def set_temperature():
    temp = parseThis('Temperature')

    if temp > 24 or temp < 14:
        answer = speak("Your temperature level is at an unwanted level right now")
    else:
        answer = speak("Your readings appear normal right now")

    return answer


#Gives a specific reading from your database... "What is the {co2/temp/hum} level in the {room}"
def get_reading():

    return "Your {temp} in the bathroom right now is {reading}"


#Gives readings from a specific date... "Your {co2/temp/hum} reading in the {room} on the {date} is..."
def from_this_day():

    return "On the {date} your {co2/temp/hum} readings are {reading} in the {room} "


#Gives all your house units temperatures...
def all_temp():
    command = take_command()
    if 'electron' in command:
        if 'temperature' and 'all' in command:
            talk("In the garage, your reading is at ")
            talk(tempVals[garage])
            talk('degrees')
            talk("In the kitchen, your reading is at ")
            talk(tempVals[kitch])
            talk('degrees')
            talk("In the bedroom, your reading is at ")
            talk(tempVals[bedR])
            talk('degrees')
    else:
        command2 = "why did you not tell me"
       #command2 = take_command()
        if 'why' and 'not' in command2:
          talk("I am not telling you, because you never said my name!")



#GIves all units humidity...
def all_hum():
    command = take_command()
    if 'electron' in command:
        if 'humidity' and 'all' in command:
            talk("In the garage, your reading is at ")
            talk(humVals[garage])
            talk('percent')
            talk("In the kitchen, your reading is at ")
            talk(humVals[kitch])
            talk('percent')
            talk("In the bedroom, your reading is at ")
            talk(humVals[bedR])
            talk('percent')
    else:
        command2 = "why did you not tell me"
       #command2 = take_command()
        if 'why' and 'not' in command2:
          talk("I am not telling you, because you never said my name!")


#all_hum()


#Gives all CO2 readings...
def all_co2():
    command = take_command()
    if 'electron' in command:
        if 'c. o. two' and 'all' in command:
            talk("In the garage, your reading is at ")
            talk(co2Vals[garage])
            talk('ppm')
            talk("In the kitchen, your reading is at ")
            talk(co2Vals[kitch])
            talk('ppm')
            talk("In the bedroom, your reading is at ")
            talk(co2Vals[bedR])
            talk('ppm')
    else:
        command2 = "why did you not tell me"
       #command2 = take_command()
        if 'why' and 'not' in command2:
          talk("I am not telling you, because you never said my name!")


#Sets a reminder to check your sensor
#Add on - Maybe set to play readings at certain time of the day?
def create_reminder():
    command = take_command()
    if 'electron' in command:
        if 'set' and 'reminder':

            return "Your reminder has been set."


#Gives Hum, CO2 and Temp readings of every unit in your house..
#necessary????

#def all_data():

    #return "Your house unit readings are as follows, "
