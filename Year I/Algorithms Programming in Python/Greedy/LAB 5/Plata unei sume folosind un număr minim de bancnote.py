# 4. Plata unei sume folosind un număr minim de bancnote
# Fie o mulțime de bancnote {BB0, BB1, ... , BBnn} astfel încât BB0 = 1 (avem mereu bancnota unitate,
# pentru a putea plăti orice sumă) și BBii|BBjj, ∀ 0 ≤ ii < jj ≤ nn − 2 (cu excepția ultimelor 2 bancnote,
# toate valorile se divid cu toate valorile din listă mai mici decât ele). De exemplu se consideră
# bancnotele românești cu valorile {1, 5, 10, 50, 100, 200, 500}.
# Pentru o sumă de bani S, să se determine o modalitate de a plăti suma S folosind un număr minim
# de bancnote. Fișierul “bani.txt” conține pe prima linie valorile bancnotelor disponibile (se consideră că
# avem la dispoziție un număr infinit din fiecare bancnotă), iar pe a doua linie valoarea sumei S. În
# fișierul “plata.txt” să se afișeze ce bancnote cu valori diferite și câte din fiecare valoare s-au folosit
# pentru a achita suma S.

f = open("bani.txt", "r")
v = []
x = f.readline().split()
for i in x:
    v.append(int(i))
n = int(f.readline())
v.sort(reverse=True)
f.close()

print(n, "=", end=" ")
for i in v:
    ala = 0
    if int(i) < n:
        while int(i) <= n:
            ala += 1
            n -= int(i)
    if ala:
        if n:
            print(i, "*", ala, "+", end=" ")
        else:
            print(i, "*", ala, end=" ")

