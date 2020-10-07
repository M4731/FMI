"""
1. Într-o propoziție/frază a fost efectuată, posibil de mai multe ori, aceeași greșeală de ortografie.
Scrieți un program care citește propoziția, șirul greșit și șirul corect, după care afișează propoziția
corectă. De exemplu, în propoziția “Problemele cu șiruri de caractedf nu sunt gdfle!” greșeală constă
în faptul că în loc de șirul “re” a fost scris șirul “df”.
"""
n = str(input("text: "))
g = str(input("greseala: "))
c = str(input("corect: "))
w = n.replace(g,c)
print("text final:",w)