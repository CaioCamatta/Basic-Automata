### Basic Automata.
### I made this automata to understand how automatas work.
### This code was not polished to run faster and use less memory, that's not its purpose. It's actually very slow.
### By Caio Camattta 

import random

# Initial numbers. Change as you will. Use random_initial() if you want to randomize this
initial_grid = [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]

# Generate random initial_grid, with a lenght of 'number'
def random_initial(number):
		global initial_grid
		initial_grid = []
		for i in range(number):
			initial_grid.append(random.choice('01'))



# Neighborhood rules, you can play around with these values
rules = {'000': '1', '001': '0', '010': '0', '011': '0', '100': '0', '101': '0', '110': '1', '111': '1'}


# Empty list. Values will be added on every iteration
new_grid = []

def next_grid(grid):
	global new_grid
	new_grid = []
	for index in range(len(grid)):
		if index != len(grid)-1:
			# PREVIOUS, INDEX, NEXT
			case = str(grid[index-1]) + str(grid[index]) +str(grid[index+1])

			# In case it's the last value of the list. grid[index+1] would not work like PacMan and return to the first value of the list
		else:
			case = str(grid[index-1]) + str(grid[index]) +str(grid[0])
		
		new_grid.append(int(rules[case]))


	# Convert 1,0 to ' ,■' respectively (Better visualization)
	converted_grid = []
	for index in range(len(new_grid)):
		if new_grid[index]==0:
			converted_grid.append(' ')
		if new_grid[index]==1:
			converted_grid.append('■')
	print(''.join(map(str, converted_grid)))


random_initial(80) # Generate random initial_grid.
next_grid(initial_grid)
for i in range(0,50): # Number of times the function will repeat
	next_grid(new_grid)
	
