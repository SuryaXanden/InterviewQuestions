limit = int(input("Enter the number of lines to generate the pattern: "))
all = [[None for j in range(limit)] for i in range(limit)] #Creation of an empty list
insertAt = 0
T = 0       # Top line
B = limit       # Bottom line
oddEven = 1     # 1 => odd & 0 => even
count = 1       # count is the item in the patter ranging from 1 to limit**2
for itr in range(limit):
    if oddEven:
        insertAt = T        # Inserting the generated numbers at the top line
        B -= 1      # decrement bottom (to move upwards)
    else:
        insertAt = B        # Inserting the generated numbers at the bottom line
        T += 1      # increment top (to move downwards)
    for i in range(limit):
        all[insertAt][i] = count
        count += 1
    oddEven = not oddEven       # toggle oddEven
for i in range(limit):
    for j in range(limit):
        print(all[i][j],end=" ")        # printing
    print()