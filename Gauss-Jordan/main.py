import random as r
import string

# Random exercise, and also an answer generation
def random(size):
    equations = []
    for e in range(0, size[1]): # For each equation
        equations.append([])
        for var in range(0, size[0]): # For each variable inside an equation
            equations[e].append(r.randint(-5, 5))
        equations[e].append(r.randint(-5, 5))
    
    return equations, 0

# Solve user's system

# Interface with the user
print("\n\nWelcome to Gauss-Jordan python project!\n\nIf you need help, type 'h'\n\n")

while True:
    userInput = input("-> ")

    if userInput == "h": # Help
        print("\nList of commands:\n0 - END;\nh - help;\nrandom - Random exercise;\nsolve - Solve a system given by the user;\n")
    
    if userInput == "0": 
        print("\nClosing...\n")
        break

    if userInput == "random":
        print("\nEntering the random mode, please type the size of the system.\n")
        size = []
        while len(size) != 1:
            try:
                num = input("Type the number of variables: ")
                size.append(int(num))
            except:
                print("Please type a valid number.\n")
        while len(size) != 2:
            try:
                num = input("Type the number of equations: ")
                size.append(int(num))
            except:
                print("Please type a valid number.\n")
        
        system, answer = random(size)

        print("\n")
        alpha = list(string.ascii_lowercase) # Alphabet
        for e in system: # For equation
            text = ""
            for i in range(0, len(e)-1): # For variable (except the last one)
                text += f"{'' if e[i]<0 else '+'}{e[i]}{alpha[i]} "
            text += f"= {'' if e[-1]<0 else '+'}{e[-1]}"
            print(f"{text}")
        
        print("\n")
        
        while True:
            a = input("Do you want to see the answer? [Y/N] -> ").upper()
            if a == "N": 
                break
            elif a == "Y":
                print(f"{answer}\n")
                break

