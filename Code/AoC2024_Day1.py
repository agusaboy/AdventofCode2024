#Advent of Code 2024 Day 1


#Get input lists
listA = []
listB = []

with open("C:\\Users\\agusa\\OneDrive\\Documents\\GitHub\\AdventofCode2024\\Inputs\\Advent_of_code_Day1_input.txt", 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    #print(lines)

for line in lines:
    columns = line.split()
    listA.append(columns[0])
    listB.append(columns[1])


listA.sort()
listB.sort()
#print(listA)

#GET lists differences
list_diff= []
for a,b in zip(listA,listB):
    diff = int(a)-int(b)
    if diff<0:
        difference = -diff
    else:
        difference = diff
    list_diff.append(difference)
#print(list_diff)

total = 0
for ld in list_diff:
    total += ld
#print(total)

#Get similarities
similarity = 0
similarity_counts = []


for a in listA:
    sim = listB.count(a)*int(a)
    similarity_counts.append(sim)
#print(similarity_counts)

for sc in similarity_counts:
    similarity += sc

#Outputs ******************************************************************************
solutions = "Total difference is {} and similarity is {}".format(total,similarity)
print(solutions)



