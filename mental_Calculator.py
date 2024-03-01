import random
   
   
# Initialize operators
operators = ["+", "-", "*"]

# Initialize the smallest and biggest opperand
min_operand = 1
max_operand = 15
total_problems = 5

def generate_problem():
    first_Num = random.randint(min_operand, max_operand)
    second_Num = random.randint(min_operand, max_operand)
    # Random operator is chosen
    operator = random.choice(operators)
    
    # Expression consisting of left number and right number as a string
    expr = str(first_Num) +  " " + operator + " " + str(second_Num) 
    answer = eval(expr)
    return expr, answer

    # Store the answer of the operation     

for i in range (total_problems):
    expr, answer = generate_problem()
    while True:
        try:
            guess = int(input("Problem No. " + str(i+1) + ": " + expr + " = "))
            if guess == answer:
                print("Richtig")
                break
            else:
                print("Falsch, versuche es nochmal")
        except ValueError:
            print("Gib Zahl ein")