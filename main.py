import json
import random

while True:

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
    m = int(input("Your answer: "))
    user_answer = options[m-1]

    def answer_checker():
        if user_answer == exercise1["answer"]:
            return "Correct!"
        return "Incorrect.\nCorrect answer: "+exercise1["answer"]+"\n"+exercise1["explanation"]

    print(answer_checker())

    response = input("|Press Enter for next task|\n|or type q to quit|")

    if response == "q":
        break
    continue

