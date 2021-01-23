f = open("activitati.in","r")
lista_intervale = []

nr_activitati = int(f.readline())
l = [int(i) for i in f.readline().split()]
nr_intervale = int(f.readline())
for i in range(nr_intervale):
    r = f.readline()
    lista_intervale.append((int(r.split()[0]),int(r.split()[1])))


tati = [0]*nr_activitati
inceput = [0]*nr_activitati

kid = {i:[] for i in range(nr_activitati)}

for i in lista_intervale:
    kid[i[0]-1].append(i[1]-1)
    tati[i[1]-1] += 1

q = []

for i in range(nr_activitati):
    if tati[i] == 0:
        q.append(i) 

maxi = -1
max_id = -1
i=-1
last = [-1]*nr_activitati

while len(q) != nr_activitati:
    i += 1
    indice_curent = q[i]
    for x in kid[indice_curent]:
        if inceput[x] < inceput[indice_curent] + l[indice_curent]:
            inceput[x] = inceput[indice_curent] + l[indice_curent]
            if inceput[x] + l[x] > maxi:
                max_id = x
                maxi = inceput[x] + l[x]
            last[x] = indice_curent
        tati[x] -= 1
        if tati[x] == 0:
            q.append(x)

print("timp minim "+str(maxi))
print("activitati critice",end=" ")
while max_id != -1:
    print(max_id+1,end=" ")
    max_id = last[max_id]
print()
for i in range(nr_activitati):
    print(i,end=" : ")
    print(str(inceput[i])+" "+str(inceput[i]+l[i]))


# print(inceput)
# print(nr_activitati)
# print(l)
# print(nr_intervale)
# print(lista_intervale)
# print(kid)
# print(tati)

f.close()