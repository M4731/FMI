--import Numeric.Natular()
import Data.Char   
import Data.List

mmr99 :: String -> Bool -- functie ajutatoare pentru a verifica daca un cuvant este palindrom
mmr99 s = s == reverse s
--ne ajutam de functia reverse care creeaza rasturnatul lui s 
--si dupa verificam daca acestea sunt egale

--1

mmr11 :: [String] -> Bool
mmr11 [] = False
mmr11 (h:t)
    | mmr99 h = True
    | otherwise = t'
    where t' = mmr11 t

-- *Main> mmr11 ["abbaz","4132ae","examen"]
-- False
-- *Main> mmr11 ["abba","4132ae","examen"] 
-- True
-- *Main> mmr11 ["Matei","Soarece","cec"]   
-- True

--2

mmr12 :: [String] -> Bool
mmr12 s = length [x | x <- s, mmr99(x)] > 0

-- *Main> mmr12 ["abbaz","4132ae","examen"]
-- False
-- *Main> mmr12 ["Matei","Soarece","cec"]  
-- True
-- *Main> mmr12 ["abba","4132ae","examen"]
-- True
-- *Main> mmr12 ["222","4132ae","examen"] 
-- True

--3

mmr13 :: [String] -> Bool
mmr13 s = filter mmr99 s /= [] --filter aplica functia de palindrom pe toate elementele din s
--si le pune intr-o lista pe cele care dau true, iar daca lista nu este vida, inseamna ca s 
--are minim un palindrom

-- *Main> mmr13 ["abbaz","341324qe","examen"]
-- False
-- *Main> mmr13 ["abba","341324qe","examen"] 
-- True
-- *Main> mmr13 ["Matei","soarece","cer"]
-- False

--4    

mmr14 :: [String] -> Bool
mmr14 s = mmr13 s == mmr11 s

-- *Main> mmr14 ["Matei","soarece","cer"]
-- True
-- *Main> mmr14 ["abba","341324qe","examen"]
-- True
-- *Main> mmr14 ["abbaz","341324qe","examen"]
-- True

-- EX 2

--1

mmr2 :: String -> String
mmr2 [] = "" -- daca am ramas fara caractere se inchide functia
mmr2 (h:t) -- head si tail
    | length t == 0 = h : t' -- daca mai am un caracter si tail ul este gol pun caracterul
    | h == ' ' && (head t == '-' || head t == ' ') = t' -- daca am spatiu urmat de spatiu sau - nu afisez h
    | h == '-'  && head t == ' ' = h : tail t' -- daca am - nu pun spatiul de dupa
    | h /= ' ' || (h == ' ' && head t /= ' ' && head t /= '-') = h : t' -- daca nu este spatiu sau este spatiu si nu este urmat de spatiu sau -, atunci il punem
    where t' = mmr2 t -- repeta recursiv

-- *Main> mmr2 "Mi  -  am adus   aminte   de  tine"
-- "Mi-am adus aminte de tine"
-- *Main> mmr2 "lui Matei ii    place programarea    -     functionala."
-- "lui Matei ii place programarea-functionala."
-- *Main> mmr2 "Ma     doare           capul.   -      "
-- "Ma doare capul.-"