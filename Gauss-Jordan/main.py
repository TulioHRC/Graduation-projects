# Random exercise, and also an answer generation
def random(size):
    print(size)

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

