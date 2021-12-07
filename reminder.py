import speech_recognition as sr
import time
import schedule
from func import talk

listener = sr.Recognizer()

def remind_me(time):
    talk("Hi user, please  dont forgeet to check your enviromental sensr readings.")


job = schedule.every().day.at(time).do(remind_me)
