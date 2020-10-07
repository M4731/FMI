# Fișierul “spectacole.txt” conține, pe câte un rând, ora de început, ora de sfârșit și numele câte unui
# spectacol. Să se creeze o listă care să conțină, în tupluri formate din câte 3 șiruri de caractere, cele 3
# informații despre fiecare spectacol. Să se determine numărul minim de săli necesare k pentru a putea
# programa toate spectacolele, fără să existe suprapuneri între spectacolele din aceeași sală. În fișierul
# “sali.txt” să se afișeze k și apoi spectacolele care au fost programate în fiecare dintre cele k săli.

def os(x):
    z = x[1]
    z = z.replace(":", ".")
    return (float(z))


def oi(x):
    z = x[0]
    z = z.replace(":", ".")
    return (float(z))


f = open("evenimente.txt", "r")
g = open("sali.txt", "w")
v = []
for line in f.readlines():
    h1 = line.split("-")[0]
    line_v2 = line.split("-")[1]
    h2 = line_v2.split(" ", 1)[0]
    nume = line_v2.split(" ", 1)[1]
    v.append((h1, h2, nume))
f.close()
v.sort(key=oi)
dict = {}
dict[0] = []
dict[0].append(v[0])
w = 0
ajutor = []

for i in range(1, len(v)):
    k = False
    for x in dict.keys():
        if oi(v[i]) >= os(dict[x][-1]):
            if v[i] not in ajutor:
                dict[x].append(v[i])
                ajutor.append(v[i])
                k = True
    if k == False:
        if v[i] not in ajutor:
            w += 1
            dict[w] = []
            dict[w].append(v[i])

g.write(str(len(dict))+" sali"+'\n')
for ajutorcoaie in dict.keys():
    g.write("sala "+str(ajutorcoaie)+" : ")
    for x in dict[ajutorcoaie]:
        q = x[2].replace("\n", "")
        g.write("("+str(x[0])+"-"+str(x[1])+" "+q+") ")
    g.write('\n')



