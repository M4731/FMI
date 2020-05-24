"""
5. O metodă simplă (dar nesigură!!!) de criptare a unui text o reprezintă cifrul lui Cezar, prin care
fiecare literă dintr-un text dat este înlocuită cu litera aflată peste kk poziții la dreapta în alfabet în mod
circular. Valoarea kk reprezintă cheia secretă comună pe care trebuie să o cunoască atât expeditorul,
cât și destinatarul mesajului criptat. Decriptarea unui text constă în înlocuirea fiecărei litere din textul
criptat cu litera aflată peste kk poziții la stânga în alfabet în mod circular. Scrieți un program care să
realizeze criptarea sau decriptarea unui text folosind cifrul lui Cezar. Indicație de rezolvare: se va
utiliza formula eekk(xx) = (xx + kk) mod 26 pentru criptarea unui caracter xx folosind cheia secretă kk,
respectiv formula ddkk(xx) = (xx − kk) mod 26 pentru decriptare. De asemenea, se vor utiliza funcțiile
ord și chr pentru manipularea caracterelor.
"""
n = str(input("text: "))
k = int(input("valoare: "))
cript = ""
for i in n:
    if i == " ":
        cript += " "
    else:
        if i.isupper():
            cript += chr(((ord(i)+k) % 26)+65)
        else:
            cript += chr(((ord(i)+k) % 26)+97)

print("rezultat:", cript)