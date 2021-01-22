time = 0
tyme = 0
bridge_solution = []
articulation_solution = []
biconex_solution = []
count = 0


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


def bridge(n, list):
    v = []
    tati = [-1]*n

    disc = [-1] * n 
    low = [-1] * n 

    for i in range(n):
        if i not in v:
            DFS3(i, v, tati, disc, low, list)



def articulation(n, list):
    v = []
    tati = [-1]*n

    disc = [-1] * n 
    low = [-1] * n 

    for i in range(n):
        if i not in v:
            DFS3(i, v, tati, disc, low, list)



def DFS3(n, v, tati, disc, low, list):
    v.append(n)
    children = 0

    global time, bridge_solution, articulation_solution
    disc[n] = time 
    low[n] = time
    time += 1
    
    for i in list[n]:
        if i not in v:
            tati[i] = n
            children += 1
            DFS3(i, v, tati, disc, low, list)

            low[n] = min(low[i], low[n])

            if low[i] > disc[n] and (i,n) not in bridge_solution: 
                bridge_solution.append((i,n))
                # print("1")

            if tati[n] == -1 and children > 1:
                if n not in articulation_solution:
                    articulation_solution.append(n)
            
            if low[i] >= disc[n] and tati[n] != -1: 
                if n not in articulation_solution:
                    articulation_solution.append(n)

        elif i != tati[n]:
            low[n] = min(low[n], disc[i])


def biconex(n, list, lines):
    # print(list)
    for j in lines:
        v = j[0]
        w = j[1]
        # print((v,w))
        list[v].remove(w)
        list[w].remove(v)
    # print(list)


    tati = [-1]*n
    disc = [-1] * n 
    low = [-1] * n 

    stack = []

    for i in range(n): 
        if disc[i] == -1: 
            DFS_AUX(i, tati, low, disc, stack, list)

    


def DFS_AUX(n, tati, low, disc, stack, list):
    global count, tyme, biconex_solution
    children = 0

    solutie_locala = []
    disc[n] = tyme
    low[n] = tyme
    tyme += 1

    for i in list[n]:
        if disc[i] == -1:
            tati[i] = n
            children += 1
            stack.append((n,i))

            DFS_AUX(i, tati, low, disc, stack, list)

            low[n] = min(low[i], low[n])
        
            if tati[n] == -1 and children > 1 or low[i] >= disc[n] and tati[n] != -1:
                muchie = -1
                while muchie != (n,i):
                    muchie = stack.pop()
                    solutie_locala.append(muchie)
        elif i != tati[n] and low[n] > disc[i]:
            low[n] = min(low[n], disc[i])
            stack.append((n,i))

    
    auxiliar = []
    for i in solutie_locala:
        v = i[0]
        w = i[1]
        if v not in auxiliar:
            auxiliar.append(v)
        if w not in auxiliar:
            auxiliar.append(w)
    if len(auxiliar) > count:
        count = len(auxiliar)
        biconex_solution = solutie_locala  

    
    # print(solutie_locala)


def out():
    global bridge_solution 
    global articulation_solution 
    global biconex_solution
    auxiliar = []

    f = open("graf.out","w")

    f.write("Legaturi critice\n")
    for i in bridge_solution:
        f.write(str(i[0])+" "+str(i[1])+"\n")

    f.write("Noduri vulnerabile\n")
    for i in articulation_solution:
        f.write(str(i)+" ")
    f.write("\n")

    f.write("Subretea\n")
    for i in biconex_solution:
        v = i[0]
        w = i[1]
        if v not in auxiliar:
            auxiliar.append(v)
        if w not in auxiliar:
            auxiliar.append(w)
    for i in auxiliar:
        f.write(str(i)+" ")
    f.write("\n")
    for i in biconex_solution:
        f.write(str(i[0])+" "+str(i[1])+"\n")



f = open("graf.in","r")
list = []

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

l = f.readline()
while l:
    list.append((int(l.split()[0]), int(l.split()[1])))
    l = f.readline()

lista = lista_adiacenta(m,n,list,"neorientat")



bridge(n, lista)
articulation(n, lista)
# print(bridge_solution)
# print(articulation_solution)

biconex(n, lista, bridge_solution)

# print(biconex_solution)

f.close()

out()