import random
import re

assets = {1: "rock", 2: "paper", 3: "scissors"}  # 🪨📜✂️

currentUser = 0
scoreUser = 0
currentBot = 0
scoreBot = 0
# who = {1: "currentUser", 2: "currentBot"}


def switch():
    global currentUser
    while True:
        user = input("Choose:\n[1]Rock 🪨\n[2] Paper 📜\n[3] Scissors ✂️")

        if user.isdigit() and int(user) in range(1, 4):
            currentUser = assets.get(int(user))
            break
        else:
            print("Please enter a valid choice between 1 and 3.")

    return currentUser


def generateBot():
    global currentBot
    currentBot = assets.get(random.randrange(1, 4))
    return currentBot


def logic(User, Bot):
    global scoreUser, scoreBot
    # 👔
    if User == Bot:
        print("Tie")
    # 🪨 -> ✂️
    elif User == "rock" and Bot == "scissors":
        scoreUser += 1
        scoreBot = scoreBot
        return scoreUser, scoreBot
    # 📜 -> 🪨
    elif User == "paper" and Bot == "rock":
        scoreUser += 1
        scoreBot = scoreBot
        return scoreUser, scoreBot
    # ✂️ -> 📜
    elif User == "scissors" and Bot == "paper":
        scoreUser += 1
        scoreBot = scoreBot
        return scoreUser, scoreBot
    else:
        scoreUser = scoreUser
        scoreBot += 1
        return scoreUser, scoreBot


def picked(User, Bot):
    print("User:", User, "Bot:", Bot)


def status():
    print("User:", scoreUser, "Bot:", scoreBot)


while True:
    status()
    switch()
    generateBot()
    picked(currentUser, currentBot)
    logic(currentUser, currentBot)
    