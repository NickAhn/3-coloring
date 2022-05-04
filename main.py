vertices = 4 # number of vertices = number of lines in input file
colors = 3 # R G B

#TODO: make dictionary instead of single list

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


# numbers = [i for i in range(1, vertices * colors+1)]
# print(numbers)

i = 0
#singe color constraint

print("\nSingle Value Constraints: ")
for list in dic.values():
    for num in list:
        print(num, end = " ")
    print(0)

    for j in range(len(list)):
        for k in range(j+1, len(list)):
            print(-1*list[j], -1*list[k], "0", sep = " ")

    print() # newline TODO: delete

