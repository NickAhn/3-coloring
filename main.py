vertices = 4

input_file = open("input.txt", "r")
lines = [line.strip('\n') for line in input_file if line != "\n"] 

vertices = len(lines)  # number of vertices = number of lines in input file
colors = 3 # R G B

# create a dictionary where key = vertice letter, value = possible colors
ascii = 97 # starting at 'a'
counter = 1
dic = {}
while (counter < vertices*colors + 1):
    temp = [i for i in range(counter, counter+3)]
    dic[chr(ascii)] = temp
    counter += 3 
    ascii += 1 # next letter in alphabet

    
for key, value in dic.items():
    print(key, value, sep=" : ") 

print("\nSingle Value Constraints: ")
for list in dic.values():
    for num in list:
        print(num, end = " ")
    print(0)

    for j in range(len(list)):
        for k in range(j+1, len(list)):
            print(-1*list[j], -1*list[k], "0", sep = " ")

    print() # newline TODO: delete


def getCombinations(vert1, vert2):
    for x, y in zip(vert1, vert2):
        print(-1*x, -1*y, sep = " ", end = " 0\n")

print("Unique Color Constraints: ")
for key, line in zip(dic.keys(), lines):
    for edge in line.split():
        getCombinations(dic[key], dic[edge])
        print()


    