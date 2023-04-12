import random as r
import string

alpha = list(string.ascii_lowercase)
# Random exercise, and also an answer generation
def random(size):
    equations = []
    for e in range(0, size[1]): # For each equation
        equations.append([])
        for var in range(0, size[0]): # For each variable inside an equation
            equations[e].append(r.randint(-5, 5))
        equations[e].append(r.randint(-5, 5))

    return equations

def printEquation(system):
    print("\n") # Alphabet
    for e in system: # For equation
        text = ""
        for i in range(0, len(e)-1): # For variable (except the last one)
            text += f"{'' if e[i]<0 else '+'}{e[i]}{alpha[i]} "
        text += f"= {'' if e[-1]<0 else '+'}{e[-1]}"
        print(f"{text}")

    print("\n")

def receiveSize():
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

    return size
# Solve system
def solve(matrice):
    print("\nSolving...\n")

    pivot = 0 # Which pivot is being used
    newMatrice = matrice
    for index in range(0, len(matrice)):
        #print(f"\n{pivot} - Pivot")
        for increment in range(0, len(matrice)-index): # Switch positions if pivot 0
            if newMatrice[index][pivot] != 0: break
            newMatrice[index], newMatrice[index+increment] = newMatrice[index+increment], newMatrice[index]
        #print(newMatrice)
        for i in range(len(newMatrice[index])-1, -1, -1): # For each element of the row (pivot turns 1)
            if newMatrice[index][pivot] == 0: break # If all of the pivot's columns are 0, skips it
            newMatrice[index][i] = newMatrice[index][i]/newMatrice[index][pivot]
        #print(newMatrice)
        for row in range(0, len(matrice)): # Pivot's column turns into 0 (except the pivot)
            if not row == index and newMatrice[index][pivot] != 0:
                change = newMatrice[row][pivot]
                for e in range(0, len(newMatrice[row])):
                    newMatrice[row][e] -= newMatrice[index][e]*change
        #print(newMatrice)
        pivot += 1 if newMatrice[index][pivot] != 0 else 2


    return newMatrice


# Interface with the user
print("\n\nWelcome to Gauss-Jordan python project!\n\nIf you need help, type 'h'\n\n")

while True:
    userInput = input("-> ")

    if userInput == "h": # Help
        print("\nList of commands:\n0 - END;\nh - help;\nrandom - Random exercise;\nsolve - Solve a system given by the user;\n")

    if userInput == "0":
        print("\nClosing...\n")
        break

    if userInput == "test":
        #print(f"\n{solve([[5,5,0,15],[2,4,1,10],[3,4,0,11]])}\n")
        print(f"\n{solve([[1,2,0,0,3],[0,0,1,0,0],[0,0,0,1,-4]])}\n")

    if userInput == "solve":
        # Manual mode
        print("\nEntering the manual mode, please type the size of the system.\n")

        size = receiveSize()
        system = []

        for row in range(0, size[1]):
            system.append([])
            print(f"Equation {row+1}: ")
            for variable in range(0, size[0]+1):
                if variable == (size[0]):
                    num = float(input("= "))
                else:
                    num = float(input(f"{alpha[variable]}."))
                system[row].append(num)
            print("\n")

        printEquation(system)
        resolution = solve(system)
        printEquation(resolution)


    if userInput == "random":
        print("\nEntering the random mode, please type the size of the system.\n")

        size = receiveSize()
        system = random(size)

        printEquation(system)

        while True:
            a = input("Do you want to see the answer? [Y/N] -> ").upper()
            if a == "N":
                break
            elif a == "Y":
                resolution = solve(system)
                printEquation(resolution)
                break
