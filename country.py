"""
This program is based on simple design on chat bot..
1.The bot starts with greeting, self introduction  
and ask for the name of the person
2.The bot will greet and welcome the person
3.Bot will ask the person want to do, it will offer a
choice of things based upon the bot design
4.It will respond to users to input correctly
"""
from datetime import datetime
from greetings import greet_and_introduce,welcome
import pycountry_convert as pc

def show_menu():
    print("1.Calculate an expression")
    print("2.get continent from country.")
    print("3.End this chat")
    print("-----------------------------------------------------")
    try:
        return int(input("Enter your choice from [1-3]: "))
    except:
        print("Oops,you must enter a number from [1-3]")
        return 0

def evaluate_expression():
    expr = input("Enter an expression")
    try:
        print("Result = ",eval(expr))
    except Exception as e:
        print(str(e))


def country_to_continent():
    country_name = input("country name = ")
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    print(country_continent_name)


    

def bot():
    greet_and_introduce()
    name = input("your name: ")
    welcome(name)
    choice =show_menu()
    while choice != 3:
        if choice == 1:
            evaluate_expression()
        elif choice ==2:
            country_to_continent()
        else:
            print("I dont understand that")
        choice = show_menu()
    bot()
bot()
