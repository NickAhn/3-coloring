vertices = 4 # number of vertices = number of lines in input file
colors = 3 # R G B

#TODO: make dictionary instead of single list
numbers = [i for i in range(1, vertices * colors+1)]
print(numbers)

i = 0
#singe color constraint
print("\nSingle Color Constraint:")
while i < len(numbers):
    temp = numbers[i: (i+3)] # A_r A_g A_b ...
    for vertice in temp:
        print(vertice, " ", end="")

    print() # new line
    for j in range(len(temp)):
        for k in range(j+1, len(temp)):
            print(-1*temp[j], -1*temp[k], "0", sep=" ")

    print()
    i += 3

