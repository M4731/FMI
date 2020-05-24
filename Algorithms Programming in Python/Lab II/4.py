"""
4. Scrieți un program care să se verifice dacă două șiruri de caractere sunt anagrame sau nu. Două
șiruri sunt anagrame dacă unul se poate obține din celălalt printr-o permutare a caracterelor sale. De
exemplu, șirurile emerit și treime sunt anagrame, dar șirurile emerit și treimi nu sunt! Indicație de
rezolvare (fără structuri de date auxiliare și fără sortare): Se caută, pe rând, fiecare caracter din
primul șir în cel de-al doilea. În cazul în care caracterul nu este găsit înseamnă că șirurile nu sunt
anagrame, altfel se șterge caracterul din cel de-al doilea șir și se trece la următorul caracter din
primul șir. Atenție, folosind această metodă, cel de-al doilea șir va fi modificat!
"""
x1 = str(input("primul sir: "))
x2 = str(input("al doilea sir: "))
ok = 1
for i in x1:
    if i in x2:
        x2 = x2.replace(i, "", 1)
    else:
        ok = 0
if ok == 0:
    print("cuvintele nu sunt anagrame.")
else:
    print("cuvintele sunt anagrame.")