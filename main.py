import json
import random

with open("data/connectors.json") as file:
    exercises = json.load(file)

exercise1 = random.choice(exercises)
options = exercise1["options"]

def answer_options():
    result = ""
    for n in range(len(options)):
        result += str(n+1) + ". "+ options[n] + "\n"
    return result

print(exercise1["question"])
print(answer_options())

user_answer = options[int(input("Your answer: "))-1]

def answer_checker():
    if user_answer == exercise1["answer"]:
        return "Correct!"
    return "Incorrect.\nCorrect answer: "+exercise1["answer"]+"\n"+exercise1["explanation"] 

print(answer_checker())

