intx = inty = finx = finy = 0
inp = input('').split(' ')
intx = int(inp[0])
inty = int(inp[1])
directions = str(input(r''))
for i in range(0,len(directions)):
    if(directions[i].upper()=='N' or directions[i].upper()=='S' or directions[i].upper()=='E' or directions[i].upper()=='W'):
        tempspc = i + 1
        tempi = i
        for tempi in range(tempspc, len(directions)):
            if(directions[tempi]==','):
                tempi -= 1
                break
        val = int(directions[tempspc:tempi+1])
        if(directions[i]=='N'):
            finy += val
        if(directions[i]=='S'):
            finy -= val
        if(directions[i]=='E'):
            finx += val
        if(directions[i]=='W'):
            finx -= val
pytho = ((finx-intx)**2 + (finy-inty)**2)**(0.5)
print(finx,finy)
print(pytho)
