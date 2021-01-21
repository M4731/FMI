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

def BFS2(start, list, control):
    v = []
    tati = [-1]*len(list)
    q = queue.Queue()
    q.put(start)
    rez = []

    while not q.empty():
        nod = q.get()

        if nod in control:
            while nod !=  -1:
                rez.append(nod)
                nod = tati[nod]
            return rez
        if nod not in v:
            v.append(nod)
            for i in list[nod]:
                q.put(i)
                tati[i] = nod


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
o = "orientat"

l = f.readline()
n = int(l.split()[0])
m = int(l.split()[1])

for i in range(m):
    l = f.readline()
    list.append((int(l.split()[0]), int(l.split()[1])))

l = f.readline()
for i in l.split():
    control.append(int(i)-1)

#a = int(input("Punct de plecare: "))-1
a = 0

lista = lista_adiacenta(n,m,list,o)
bf = BFS(a, lista)

for i in bf:
    if i in control:
        sal = i
        break

result = BFS2(a, lista, control)

f.close()

f = open("graf.out","w")

for i in range(len(result)-1,-1,-1):
    f.write(str(result[i]+1)+" ")

print (bf)
# print (list)
print (control)
# print(a)

f.close()