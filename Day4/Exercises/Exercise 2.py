data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def quiz():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for question_data in data:
        question = question_data["question"]
        correct_answer = question_data["answer"]

        user_answer = input(question + " ").capitalize()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect!")
            incorrect_answers += 1
            wrong_answers.append({
                "question": question,
                "user_answer": user_answer,
                "correct_answer": correct_answer
            })

    return correct_answers, incorrect_answers, wrong_answers


def display_results(correct, incorrect, wrong_answers):
    print(f"\nYou got {correct} correct answers and {incorrect} incorrect answers.")
    if incorrect > 0:
        print("\nHere are the questions you answered incorrectly:")
        for answer in wrong_answers:
            print(f"\nQuestion: {answer['question']}")
            print(f"Your answer: {answer['user_answer']}")
            print(f"Correct answer: {answer['correct_answer']}")
    if incorrect > 3:
        print("\nYou had more than 3 wrong answers. You can play again if you want.")


def main():
    correct, incorrect, wrong_answers = quiz()
    display_results(correct, incorrect, wrong_answers)


if __name__ == "__main__":
    main()