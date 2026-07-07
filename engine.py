import json

def answer_checker(user_answer, exercise):
    correct = exercise["answer"]
    options = exercise["options"]

    if options[user_answer - 1] == correct:
        print("\nCorrect!")
    else:
        print("\nIncorrect.")
        print("\nCorrect answer:", correct)
        print(exercise["explanation"])