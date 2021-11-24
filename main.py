import pyttsx3
import datetime
import speech_recognition as sr
import json

#Opening my json Database
f = open('units.json',)

#Parse Func for my data
def parseThis():
    units = json.loads(f)

    for i in units['Humidity']:
       answer = print(i)

    f.close()

    return answer


#Creating enviroment for my assistnt
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("hello this is Electron the Ei home assistant")


#Function to speak current time
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

time()


#Func to speak current date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)

date()


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

greet_me()


#speech recognition function...
def take_command():
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

take_command()


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

    return "your temperature readings are as follows, "


#GIves all units humidity...
def all_hum():
    humidity = parseThis()
    answer = print("your humidity readings are as follows, " + humidity + "percent")

    return answer

#all_hum()




#Gives all CO2 readings...
def all_co2():

    return "your CO2 readings are as follows, "


#Gives Hum, CO2 and Temp readings of every unit in your house..
def all_data():

    return "Your house unit readings are as follows, "


#Sets a reminder to check your sensor
#Add on - Maybe set to play readings at certain time of the day?
def create_reminder():

    return "Your reminder has been set."
