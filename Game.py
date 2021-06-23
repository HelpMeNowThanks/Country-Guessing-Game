import Countries
import random as rd
import time
import datetime as dt
today = dt.datetime.today()
scorelist = open("scores.txt", "a")

print("Remember to capitalize first letter!")

def answerCountry():
    score = 0
    while 2 < 3:
        country, capital = rd.choice(list(Countries.Countries.items()))
        print(capital)
        answer = input("> ")
        if answer == country:
            print("Correct!")
            score += 1
            time.sleep(1)
        elif answer != country:
            print("Wrong!")
            print(f"Your final score was {score}")
            time.sleep(2)
            scorelist.write(f"Date: {today} - Game: Guess the country - Score: {score}\n")
            scorelist.close()
            break
        elif answer == "stop":
            break

def answerCapital():
    score = 0
    while 2 < 3:
        country, capital = rd.choice(list(Countries.Countries.items()))
        print(country)
        answer = input("> ")
        if answer == capital:
            print("Correct!")
            score += 1
            time.sleep(1)
        elif answer != capital:
            print("Wrong!")
            print(f"Your final score was {score}")
            time.sleep(2)
            scorelist.write(f"Date: {today} - Game: Guess the Capital - Score: {score}\n")
            scorelist.close()
            break
        elif answer == "stop":
            break
        elif answer == "stop":
            break
def gameList():
    print("Hello! Which game?")
    print("Type 'stop' to leave!")
    print("1. Answer with Country")
    print("2. Answer with Capital")
    gameSelector = input("> ")
    if gameSelector == "1":
        answerCountry()
    elif gameSelector == "2":
        answerCapital()
    time.sleep(1)
gameList()