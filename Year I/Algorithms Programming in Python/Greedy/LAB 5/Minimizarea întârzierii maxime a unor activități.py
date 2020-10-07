# 5. Minimizarea întârzierii maxime a unor activități
# Fie o mulțime de n activități. Fiecare activitate are o anumită durată di (se execută într-un număr
# de unități de timp) și un termen limită ti până la care ar trebui executată (un număr de unități de timp
# indicat de la începutul programării tuturor activităților t0 = 0). O activitate care începe la momentul si
# și se termină la momentul fi = si + di are o întârziere de hi = max{0, fi - ti} unități de timp. Se cere
# programarea activităților astfel încât să se minimizeze întârzierea maximă H = max(hi).
# Fișierul “activitati.txt” conține pe prima linie numărul de activități n, iar pe următoarele n linii
# conține câte două numere indicând durata și termenul limită al fiecărei activități. Să se afișeze în
# fișierul “intarzieri.txt” programarea activităților, pe câte o linie, astfel: intervalul ales (si --> fi), de
# lungime egală cu durata di, termenul limită ti și întârzierea hi pentru fiecare activitate. Pe ultima linie
# din fișier să se afișeze întârzierea maximă.


def os(x):
    return x[1]


def timp(x):
    return x[0]


f = open("activitati.txt", "r")
g = open("intarzieri.txt", "w")
n = int(f.readline())
v = []
for i in range(n):
    w = f.readline().split()
    v.append((int(w[0]), int(w[1])))
v.sort(key=os)
f.close()
g.write("Interval / Termen / Intarziere")
g.write("\n")

intmax = 0
ora = 0
for i in range(n):
    g.write("("+str(ora)+" -> ")
    ora += timp(v[i])
    g.write(str(ora)+") / ")
    g.write(str(os(v[i]))+" / ")
    intarziere = ora - os(v[i])
    if intarziere > 0:
        g.write(str(intarziere))
        intmax += intarziere
    else:
        g.write("0")
    g.write("\n")
g.write("Intarzierea maxima: "+str(intmax))
g.close()