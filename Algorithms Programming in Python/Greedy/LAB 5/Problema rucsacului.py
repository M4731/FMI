# Se consideră n obiecte, pentru fiecare cunoscând valoarea și greutatea sa. Având la dispoziție un
# rucsac în care se pot încărca obiecte (sau fragmente de obiecte) în limita unei greutăți maxime date,
# să se determine o încărcare optimală a rucsacului, respectiv valoarea totală a obiectelor din rucsac să
# fie maximă.
# Fișierul “obiecte.txt” are pe prima linie numărul de obiecte n, pe următoarele n linii câte două
# numere (valoarea și greutatea obiectului curent), iar la final greutatea maximă care se poate încărca
# în rucsac. În fișierul “rucsac.txt” să se afișeze obiectele încărcate în rucsac, precum și valoarea
# acestora.


def function(w):
    return w[0]/w[1]


f = open("obiecte.txt", "r")
g = open("rucsac.txt", "w")
n = int(f.readline())
v = []
for i in range(n):
    x = f.readline().split()
    v.append((int(x[0]), int(x[1])))
greutate = int(f.readline())
v.sort(key=function, reverse=True)
f.close()
rez = []
print(v)
g.write("greutate: "+"\n")
g.write(str(greutate) + " = ")
a = 0

for i in v:
    if i[1] < greutate:
        rez.append(i)
        greutate -= i[1]
        a += i[0]
    else:
        x = greutate / i[1]
        rez.append(i)
        a += (i[0]*x)
        break
for i in range(len(rez)-1):
    g.write(str(rez[i][1])+" + ")
g.write(str(int(x*100))+"%"+str(rez[len(rez)-1][1]))
g.write('\n')

g.write("valoare obiecte din rucsac: "+"\n")
g.write(str(a) + " = ")
for i in range(len(rez)-1):
    g.write(str(rez[i][0])+" + ")
g.write(str(int(x*100))+"%"+str(rez[len(rez)-1][0]))