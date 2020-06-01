# 2. Programarea spectacolelor
# Fișierul “spectacole.txt” conține, pe câte un rând, ora de început, ora de sfârșit și numele câte unui
# spectacol. Să se creeze o listă care să conțină, în tupluri formate din câte 3 șiruri de caractere, cele 3
# informații despre fiecare spectacol.
# Să se programeze într-o singură sală un număr maxim de spectacole care să nu se suprapună. În
# fișierul “programare.txt” să se afișeze, pe câte un rând, intervalul de desfășurare și numele pentru
# spectacolele selectate.


def os(x):
    z = x[1]
    z = z.replace(":", ".")
    return(float(z))


def oi(x):
    z = x[0]
    z = z.replace(":", ".")
    return(float(z))


f = open("spectacole.txt", "r")
g = open("programare.txt", "w")
v = []
for line in f.readlines():
    h1 = line.split("-")[0]
    line_v2 = line.split("-")[1]
    h2 = line_v2.split(" ", 1)[0]
    nume = line_v2.split(" ", 1)[1]
    v.append((h1, h2, nume))
f.close()
v.sort(key=os)

g.write(v[0][0]+"-"+v[0][1]+" "+v[0][2])
last = v[0]
for x in v:
    if oi(x) > os(last):
        g.write(x[0]+"-"+x[1]+" "+x[2])
        last = x
g.close()
