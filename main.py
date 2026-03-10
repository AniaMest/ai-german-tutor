
from exercises import exercise_loader, exercise_chooser
from userInterference import question_display, get_user_answer, quitting
from engine import answer_checker

def main():
    exercises = exercise_loader()

    while True:
        exercise = exercise_chooser(exercises)

        question_display(exercise)

        user_answer = get_user_answer(len(exercise["options"]))

        answer_checker(user_answer, exercise)

        if not quitting():
            break

if __name__ == "__main__":
    main()
        




