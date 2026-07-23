import json

def question_display(exercise):
    print(exercise["question"])
    
    for i, option in enumerate(exercise["options"], start=1):
        print(f"{i}. {option}")

def get_user_answer(option_nums):
    while True:
        answer = input("\nYour answer: ")

        if not answer.isdigit():
            print("\nYou must enter a number.")
            continue

        answer = int(answer)

        if 1 <= answer <= option_nums:
            return answer
        
        print("\nInvalid answer. Try again.")

def quitting():
    while True:
        response = input("\n|Press Enter for next task|\n|or type q to quit|\n")
        
        if response == "":
            return True
        if response == "q":
            return False
        print("\nInvalid response.")


