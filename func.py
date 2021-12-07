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


##https://www.ibm.com/cloud/watson-speech-to-text for when i want totrain the voice data. I will send it to an api and train it and send it back

#Parse Func for my data
def parseThis(x):
    with open('units.json', 'r') as f:
        home_unit = json.load(f)

    for value in home_unit:

        answer = print(value[x])

    return answer


#Listener...1
listener = sr.Recognizer()

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
            print("Listening...")
            #listen to your voice as the source
            voice = listener.listen(source)
            #pass the audio to google and google returns text
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)

            userInput =  command

            #only prints what you say if electron is said
            #if 'electron' in command:
                #this removes 'electron from the string while having it as a wake word still
                #command = command.replace('electron', '')
               # talk(command) #will repeat back to you what you said
    except:
        command = ''

    return command



#Function to speak current time
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print("Time: " + str(Time))


#Func to speak current date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)

    print("Date: " + str(day) + "/" + str(month) + "/" + str(year))



#Func to greet our user with time sensitivty
def greet_me():

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        talk("Good Morning user!")
    elif hour >= 12 and hour <18:
         talk("Good afternoon user!")
    else:
         talk("Good evening user!")

    talk("How can I help you?")



def bedroom_unit(x):

        x = x.lower()

        #if the user asks for any of theses values they will be spoken
        if 'temperature' in x:
                            talk(str(tempVals[bedR]) + 'degrees')

        elif 'c. o. two' in x:
                            talk(str(co2Vals[bedR]) + 'ppm')

        elif 'humidity' in x:
                            talk(str(humVals[bedR]) + 'percent')


def kitchen_unit(y):

        y = y.lower()

        #bedroom must be spoken for this to activate
                #if the user asks for any of theses values they will be spoken
        if 'temperature' in y:
                        talk(str(tempVals[kitch]) + 'degrees')

        elif 'c. o. two' in y:
                        talk(str(co2Vals[kitch]) + 'ppm')

        elif 'humidity' in y:
                        talk(str(humVals[kitch]) + 'percent')


def garage_unit(z):

        z = z.lower()

        #if the user asks for any of theses values they will be spoken
        if 'temperature' in z:
                    talk(str(tempVals[garage]) + 'degrees')

        elif 'c. o. two' in z:
                    talk(str(co2Vals[garage]) + 'ppm')

        elif 'humidity' in z:
                    talk(str(humVals[garage]) + 'percent')



# If a temperature hits a certain level speak "Your temperature has hit an unsafe level"
def set_temperature():
    temp = parseThis('Temperature')

    try:
        #use microphone as source
        with sr.Microphone() as source:
            talk("What highest temp would you like to set?")
            #listen to your voice as the source
            voice = listener.listen(source)
            #pass the audio to google and google returns text
            high = listener.recognize_google(voice)
            high = high.lower()
            highTemp = str(high)

            talk("What lowest temp would you like to set?")
            #listen to your voice as the source
            voice = listener.listen(source)
            #pass the audio to google and google returns text
            low = listener.recognize_google(voice)
            low = high.lower()
            lowTemp = str(low)

    except:
        pass

    if temp > highTemp or temp < lowTemp:
        answer = talk("Right now, Your temperature level is at an unwanted level right now")
    else:
        answer = talk("Right now, Your readings appear normal right now")

    return answer


#Gives all your house units temperatures...
def all_temp(x):
    command = take_command()
    if 'temperature' and 'all' in x:
        talk("In the garage, your reading is at " + str(tempVals[garage]) + ' degrees')
        talk("In the kitchen, your reading is at "+ str(tempVals[kitch]) + ' degrees')
        talk("In the bedroom, your reading is at " + str(tempVals[bedR]) + ' degrees')


#GIves all units humidity...
def all_hum(y):
    command = take_command()
    if 'humidity' and 'all' in y:
        talk("In the garage, your reading is at " + str(humVals[garage]) + ' percent')
        talk("In the kitchen, your reading is at "+ str(humVals[kitch]) + ' percent')
        talk("In the bedroom, your reading is at " + str(humVals[bedR]) + ' percent')



#Gives all CO2 readings...
def all_co2(z):
    command = take_command()
    if 'c. o. two' and 'all' in z:
        talk("In the garage, your reading is at " + str(co2Vals[garage]) + ' ppm')
        talk("In the kitchen, your reading is at "+ str(co2Vals[kitch]) + ' ppm')
        talk("In the bedroom, your reading is at "  + str(co2Vals[bedR]) + ' ppm')


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


