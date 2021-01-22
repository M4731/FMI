def DFS(start, list):
    v = []
    stack = []
    v.append(start)
    stack.append(start)

    while len(stack) != 0:
        s = stack.pop()
        if s not in v:
            v.append(s)
        for i in list[s]:
            if i not in v and i not in stack:
                stack.append(i)
        
    return v

def lista_adiacenta(n,m,list,o):
    matx = [[]for i in range(n)] 

    if o == "neorientat":
        for i in list:
            matx[i[0]-1].append(i[1]-1)
            matx[i[1]-1].append(i[0]-1)
    elif o == "orientat":
        for i in list:
            matx[i[0]-1].append(i[1]-1)

    return matx

o = "neorientat"

f = open("zgraf.in","r")
list = []
o = "neorientat"

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

for i in range(m):
    l = f.readline()
    list.append((int(l.split()[0]), int(l.split()[1])))

lista = lista_adiacenta(n,m,list,o)

print(DFS(0,lista))
f.close()   