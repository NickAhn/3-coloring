input_file = open("input.txt", "r")
lines = [line.strip('\n') for line in input_file if line != "\n"] # Separate lines and ignore empty lines 

vertices = len(lines)  # number of vertices = number of lines in input file
colors = 3 # R G B

'''
create a dictionary where:
    - key = vertice letter
    - value = ID for Vertex_color (e.g. A_red = 1, A_green = 2, etc.)
'''
dic = {}
ascii = 97 # starting at 'a'
counter = 1 
while (counter < vertices*colors + 1):
    temp = [i for i in range(counter, counter+3)] # create list with all Symbols for that vertex
    dic[chr(ascii)] = temp
    counter += 3 
    ascii += 1 

    
# for key, value in dic.items():
#     print(key, value, sep=" : ") 

# print("\nSingle Value Constraints: ")
for list in dic.values():
    for num in list:
        print(num, end = " ")
    print(0)

    for j in range(len(list)):
        for k in range(j+1, len(list)):
            print(-1*list[j], -1*list[k], "0", sep = " ")

    # print() # newline TODO: delete

'''
Function to print all the unique combinations of two lists
- Used for getting constriats for unique colors between two edges
- note: we multiply by -1 to indicate negation
'''
def getCombinations(list1, list2):
    for x, y in zip(list1, list2):
        print(-1*x, -1*y, sep = " ", end = " 0\n")


'''
Unique Color Constraints
for each vertex and edges in line, 
'''
# print("Unique Color Constraints: ")
for key, line in zip(dic.keys(), lines):
    for edge in line.split():  # split() to separate each digit in lines into a list
        getCombinations(dic[key], dic[edge])  


    