import queue

def BFS(start, list):
    v = []
    q = queue.Queue()
    q.put(start)
    dist = [len(list)+1]*len(list)
    dist[start] = 0

    while not q.empty():
        # print(dist)
        nod = q.get()
        if nod not in v:
            v.append(nod)
            for i in list[nod]:
                if i not in v and dist[i] > dist[nod]+1:
                    dist[i] = dist[nod]+1
                q.put(i)
    
    return dist


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

f = open("graf.in","r")
list = []
control = []
o = "neorientat"

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

for i in range(m):
    l = f.readline()
    list.append((int(l.split()[0]), int(l.split()[1])))

l = f.readline()
s = int(l.split()[0])-1
t = int(l.split()[1])-1

lista = lista_adiacenta(n,m,list,o)

d = BFS(s, lista)

dist = d[t]

f.close()

# print(dist)
# print (lista)

ly = [[s]]

for i in ly:
    for j in range(len(lista)):
        if i[-1] == j:
            for k in lista[j]:
                y = i.copy()
                if k in y: 
                    continue
                else:
                    w = y.copy()
                    w.append(k)
                    if w not in ly:
                        ly.append(w)

for i in ly:
    if len(i) == dist+1 and i[0] == s and i[-1] == t:
        print(i)

# print(*ly,sep="\n")