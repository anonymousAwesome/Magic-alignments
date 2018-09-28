import random
with open("adjectives.txt") as input_file:
	for line in input_file:
		adjectives=line.split(", ")

colors=[]
with open("colors.txt") as input_file:
	for line in input_file:
		colors.append(line.strip())

nouns=[]
with open("realms.txt") as input_file:
	for line in input_file:
		nouns.append(line.strip())

noun=random.choice(nouns)
for i in range(5):
	color=random.choice(colors)
	adjective1=random.choice(adjectives)
	adjective2=random.choice(adjectives)
	print("The {} {}.  Known for {} and {}.".format(color,noun,adjective1,adjective2))
