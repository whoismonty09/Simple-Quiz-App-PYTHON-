quiz = {
    "What is capital of India?":
    "Delhi",
    "Which language is used for web development?":
    "Python",
    "What is 5 + 7?": "12",
    "Who developed Python?": "Guido van Rossum"
}

score = 0
print("Welcome to the Quiz developed by Monty")

for question, answer in quiz.items():
    print("\n" + question)
    user_answer = input("Your answer: ")

    if user_answer.strip().lower() == answer.lower():
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print("Correct answer is :", answer) 

print("\n Quiz Completed")
print(f"Your Score : {score}/{len(quiz)}")
           


