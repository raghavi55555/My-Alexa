import random
from datetime import datetime

def greet_and_introduce():
    responses = [
        "Nice to see you. \nI am Alexa.\nI can help you to do some calculations and you can know information about country residence.\nI believe in give and take policy so. you give me calculations and know information about country location"
    ]
    #pick a response at random and return that
    print( random.choice(responses))

def get_timeofday_greeting():
    current_time= datetime.now()
    time_Greeting="Good Morning"
    if current_time.hour>21:
        time_Greeting="Hi.Thats late"
    elif current_time.hour>16 and current_time.hour<22:
        time_Greeting="Good Evening"
    elif current_time.hour>=12 and current_time.hour<17:
        time_Greeting="Good AfterNoon"

    return time_Greeting


def welcome(name):
    messages = [
        "Nice to see you.",
        "Lets have some good time together"
    ]

    print(f"{get_timeofday_greeting()},{random.choice(messages)}")
