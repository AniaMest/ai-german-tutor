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
    
    def m_is_digit():
        global m
        m = input("Your answer: ")
        if m.isdigit():
            return True
        print("You must enter a  number.")
        return m_is_digit()
    m_is_digit()        

    def answer_validity_checker():
        if int(m) in range(1, len(options)+1):
            return True
        print("Invalid answer. Try again.")
        return m_is_digit()
    answer_validity_checker()

    user_answer = options[int(m)-1]
    def answer_checker():
        if user_answer == exercise1["answer"]:
            return "Correct!"
        return "Incorrect.\nCorrect answer: "+exercise1["answer"]+"\n"+exercise1["explanation"]


    print(answer_checker())


    def quitting():
        response = input("|Press Enter for next task|\n|or type q to quit|")
        if response == "q":
            return True
        elif response == "":
            return False
        print("Invalid response.")
        return quitting()
            

    if quitting():
        break


