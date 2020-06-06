n = int(input())
indexes = []
for i in range(n):
    indexes.append(int(input()))
indexes.sort()
min = indexes[1]-indexes[0]
for i in range( len(indexes)-1 ):
    diff = indexes[i+1] - indexes[i]
    if diff < min:
        min = diff
print(min)
