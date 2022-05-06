#Calculator
#John Hatch
num_1 = int(input("What do you want your first number to be? "))
operation = input("What do you want the operation to be? For addition(+), subtraction(-), multiplication(*), division(/) ")
num_2 = int(input("What do you want your second number to be? "))


def calc(num_1, operation, num_2):
    answer = 0
    if operation == "+":
        answer = num_1 + num_2
    elif operation == "*":
        answer = num_1 * num_2
    elif operation == "-":
        answer = num_1 - num_2
    elif operation == "/":
        answer = num_1 / num_2
    print("The answer is " + str(answer))
calc(num_1, operation, num_2)
