data Fruct = Mar String Bool
            | Portocala String Int

ionatanFaraVierme = Mar "Ionatan" False
goldenCuVierme = Mar "Golden Delicious" True
portocalaSicilia10 = Portocala "Sanguinello" 10


listaFructe = [Mar "Ionatan" False,
               Portocala "Sanguinello" 10,
               Portocala "Valencia" 22,
               Mar "Golden Delicious" True,
               Portocala "Sanguinello" 15,
               Portocala "Moro" 12,
               Portocala "Tarocco" 3,
               Portocala "Moro" 12,
               Portocala "Valencia" 2,
               Mar "Golden Delicious" False,
               Mar "Golden" False,
               Mar "Golden" True]


--1

--a

ePortocalaDeSicilia :: Fruct -> Bool
ePortocalaDeSicilia (Portocala x _) 
    | x `elem` ["Tarocco", "Moro", "Sanguinello"] = True
    | otherwise = False
ePortocalaDeSicilia _ = False

--b

nrFeliiSicilia :: [Fruct] -> Int
nrFeliiSicilia [] = 0
nrFeliiSicilia (h:t) 
    | ePortocalaDeSicilia h = (\ (Portocala f s) -> s) h + nrFeliiSicilia t
    | otherwise = nrFeliiSicilia t

--sau  

nrFeliiSicilya :: [Fruct] -> Int
nrFeliiSicilya l = sum [f | Portocala s f <- l, ePortocalaDeSicilia(Portocala s f)]

--c  

eMarCuViermi :: Fruct -> Bool
eMarCuViermi (Mar x y)
    | y = True
    | otherwise = False
eMarCuViermi _ = False

nrMereViermi :: [Fruct] -> Int
nrMereViermi [] = 0
nrMereViermi (h:t)
    | eMarCuViermi h = 1 + nrMereViermi t 
    | otherwise = 0 + nrMereViermi t


--2 

--a

data Linie = L [Int]

data Matrice = M [Linie]

verifica :: Matrice -> Int -> Bool
verifica (M matrix) i = foldr (&&) True [sum x == i | (L x) <- matrix]

test_verifica :: Bool
test_verifica = verifica (M[L[1,2,3], L[4,5], L[2,3,6,8], L[8,5,3]]) 10 == False

test_verificq :: Bool
test_verificq = verifica (M[L[2,20,3], L[4,21], L[2,3,6,8,6], L[8,5,3,9]]) 25 == True

--b

instance Show Linie where
    show (L l) = foldr (++) "" (map (\x ->( (show x)++" ")) l)

instance Show Matrice where
    show (M l) = foldr (++) "" (map (\x ->( (show x)++"\n")) l)

--c  

doarPozN :: Matrice -> Int -> Bool
doarPozN (M matrix) x =  foldr (&&) True [all (>0) nod | (L nod) <- matrix, length nod == x]

