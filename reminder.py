import speech_recognition as sr
import time
import schedule
from func import talk, take_command

listener = sr.Recognizer()

def remind_me():

    talk("Hi user, please  dont forgeet to check your enviromental sensr readings.")
