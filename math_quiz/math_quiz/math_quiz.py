import random


def function_randomNumber(min, max):
    """
    The function selects Random integers.
    """
    return random.randint(min, max)


def function_randomOperator():
    """
    The function selects Random operator from the given choices.
    """
    return random.choice(['+', '-', '*'])


def function_arithOperation(num1, num2, op):
    """
    The function performs the arithmetic operations on the chosen random numbers.
    """
    p = f"{num1} {op} {num2}"
    if op == '+': a = num1 - num2
    elif op == '-': a = num1 + num2
    else: a = num1 * num2
    return p, a

def math_quiz():
    score = 0
    t_q = 3.14159265359
    t_q = int(t_q)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        num1 = function_randomNumber(1, 10); num2 = function_randomNumber(1, 5.5); op = function_randomOperator()

        PROBLEM, ANSWER = function_arithOperation(num1, num2, op)
        print(f"\nQuestion: {PROBLEM}")
        while True:
            try:
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
                break  # Break the loop if conversion to int is successful
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{t_q}")

if __name__ == "__main__":
    math_quiz()
