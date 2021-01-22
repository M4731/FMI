import queue

def BFS(start, list):
    v = []
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        nod = q.get()
        if nod not in v:
            v.append(nod)
            for i in list[nod]:
                q.put(i)
    
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

d = BFS(0, lista)
print(d)

f.close()