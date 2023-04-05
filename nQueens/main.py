import random

# Ask for a number of queens and introduce the challenge
print("\n\n\tWelcome to the n queens challenge!!\n\n")

n = int(input("Give me a number to the n variable: "))

# Randomly create the nxn tables (1000 iterations)
tables = []
while len(tables) <= 100000:
	table = []
	queenPositions = []
	for i in range(0, n):
		row = random.randint(0, n-1)
		column = random.randint(0, n-1)
		if not (row, column) in queenPositions:
			queenPositions.append((row,column)) 

	for row in range(0, n):
		table.append([])
		for column in range(0, n):
			value = 1 if ((row,column) in queenPositions) else 0
			table[row].append(value)
	tables.append(table)

# True value for tests 8x8
#tables.append([[0,0,1,0,0,0,0,0],[1,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1],[0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0]])

# Solve with logic operators
def validate(table):
	n = len(table)
	for row in range(0, n): # Rows need to have only one queen
		if sum(table[row]) != 1:
			return False

	columns = []
	for column in range(0, n): # Columns also need to have only one queen
		columns.append([]) 
		for row in range(0, n):
			columns[column].append(table[row][column])
		if sum(columns[column]) != 1:
			return False

	for diagonal in range(0, (n*2-1)):	# Diagonal have to have only 0 or 1 queen per diagonal ´
		total = 0
		if diagonal < n: # Starts on the left side
			for pos in range(0, diagonal+1):
				if table[diagonal-pos][pos]: 
					total += 1
		else: # Starts on the right side
			for pos in range(0, n-(diagonal-n+1)):
				if table[diagonal-(n-1)+pos][n-1-pos]:
					total += 1
		if total > 1: return False

	for diagonal in range(0, (n*2-1)):	# Diagonal have to have only 0 or 1 queen per diagonal `
		total = 0
		if diagonal < n: # Starts on the right side
			for pos in range(0, diagonal+1):
				if table[diagonal-pos][n-1-pos]: 
					total += 1
		else: # Starts on the left side
			for pos in range(0, n-(diagonal-n+1)):
				if table[diagonal-(n-1)+pos][pos]:
					total += 1
		if total > 1: return False


	return True

for table in tables:
	if validate(table):
		print("Oh, one valide table.")
		for row in table: print(row)
