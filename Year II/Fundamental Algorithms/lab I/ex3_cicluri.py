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

def DFS2(start, list):
    v = []
    rez = []
    stack = []
    v.append(start)
    stack.append(start)
    tati = [-1]*len(list)

    while len(stack) != 0:
        s = stack.pop()
        if s not in v:
            v.append(s)
        for i in list[s]:
            if i not in v and i not in stack:
                stack.append(i)
                tati[i] = s
            if i in v and tati[i] != -1 and s in tati and tati[i] != s:
                # print(tati)
                # print(i)
                cop = s
                rez.append(cop)
                # print(cop)
                while i != cop and i != -1:
                    rez.append(i)
                    i = tati[i]
                    # print(cop)
                rez.append(cop)
                return(rez)
        
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

f = open("graf.in","r")
list = []
o = "neorientat"

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

for i in range(m):
    l = f.readline()
    list.append((int(l.split()[0]), int(l.split()[1])))

lista = lista_adiacenta(n,m,list,o)

DFS(0,lista)
f.close()
DFS2(1,lista)
f = open("grafex3.out","w")

kk = 0
for i in range(n-2,-1,-1):
    aoleu = DFS2(i,lista)
    if len(aoleu) != 0:
        print(aoleu)
        for j in aoleu:
            f.write(str(j+1)+" ")
            kk = 1
        break    
    if kk == 1:
        break

if kk == 0:
    f.write("nu exista cicluri in graful dat.")