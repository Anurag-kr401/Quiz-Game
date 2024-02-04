import random

def ask_question(question, options, answer):
    """
    Ask a question and return True if the user's answer is correct, False otherwise.
    """
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
        if options[int(user_answer) - 1] == answer:
            print("Correct!")
            return True
        else:
            print(f"Incorrect. The correct answer is {answer}.")
            return False
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
        return ask_question(question, options, answer)

def run_quiz():
    """
    Run the quiz and return the user's score.
    """
    questions = [
        {
            "question": "What is the maximum possible length of an identifier?",
            "options": ["16", "32", "64", "None of these above"],
            "answer": "None of these above"
        },
        {
            "question": "Who developed the Python language?",
            "options": ["Zim Den", "Guido van Rossum", "Wick van Rossum", "Niene Stom"],
            "answer": "Guido van Rossum"
        },
        {
            "question": "Which one of the following is the correct extension of the Python file?",
            "options": [".py", ".python", ".p", "None of these above"],
            "answer": ".py"
        },
        {
            "question": "In which year was the Python 3.0 version developed?",
            "options": ["2008", "2000", "2005", "2010"],
            "answer": "2008"
        },
        {
            "question": "Which of the following statements is correct regarding the object-oriented programming concept in Python?",
            "options": ["Classes are real-world entities while objects are not real", "Objects are real-world entities while classes are not real", "Both objects and classes are real-world entities", "All of the above"],
            "answer": "Objects are real-world entities while classes are not real"
        }
    ]
    random.shuffle(questions)
    score = 0
    for question in questions:
        if ask_question(question["question"], question["options"], question["answer"]):
            score += 1
    return score

if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    print("You will be given following multiple-choice questions.")
    print("Each correct answer is worth one point.")
    print("Let's begin!\n")
    score = run_quiz()
    print(f"Your final score is {score} out of 5.")