import Numeric.Natural
import Test.QuickCheck

--tot de prin lab 3 cred

numerePrimeCiur :: Int -> [Int]
numerePrimeCiur x = auxCiur [2..x]
    where 
        auxCiur [] = []
        auxCiur (h:t) = h : auxCiur [ x | x<-t, x `mod` h >0]

ordonareNat :: [Int] -> Bool
ordonareNat [] = True
ordonareNat (h:t) = and [h <= y | (h,y) <- zip(h:t) t]

ordonareNat1 :: [Int] -> Bool
ordonareNat1 [] = True
ordonareNat1 (h:t) 
    | length t == 0 = True
    | h < head t && length t == 1 = True
    | h < head t = t'
    | otherwise = False
    where t' =  ordonareNat1 t

ordonata :: [a] -> (a->a->Bool) -> Bool
ordonata (h:t) op = and [op y w | (y,w)<-zip(h:t) t]

(*<*)  :: (Integer, Integer) -> (Integer, Integer) -> Bool
(*<*) (x,y) (a,b) = and [x<a, y<b]

--compunere de functii

compuneList :: (b->c) -> [(a->b)] -> [(a->c)]
compuneList f l = map (f.) l

aplicaList :: a -> [(a->b)] -> [b]
aplicaList x l = map ($ x) l

-- aplicaList 9 (compuneList (+1) [sqrt, (^2), (/2)])
-- aplicaList 9 [sqrt, (^2), (/2)]

myzip3 :: [a] -> [b] -> [c] -> [(a,b,c)]
myzip3 l1 l2 l3 = map ( \((x,y), z) -> (x,y,z) ) (zip (zip l1 l2) l3)
-- \ e o functie ??

 --lab 4 foldr ?

--4.1

produsRec :: [Integer] -> Integer
produsRec [] = 1
produsRec (h:t) = h * t'
    where t' = produsRec t

produsFoldr :: [Integer] -> Integer
produsFoldr l =  foldr (*) 1 l

--4.2

andRec :: [Bool] -> Bool
andRec [] = True
andRec (h:t) 
    | h == True && length t == 0 = True
    | h == True = andRec t
    | otherwise = False

andFold :: [Bool] -> Bool
andFold l = foldr (&&) True l 

prop_and :: [Bool] -> Bool
prop_and l = andRec l == andFold l

--4.3

concatRec :: [[a]] -> [a]
concatRec [] = []
concatRec (h:t) = h ++ concat t

concatFold :: [[a]] -> [a]
concatFold l = foldr (++) [] l

--4.4

rmChar :: Char -> String -> String
rmChar x l = [ y | y<-l,  y/=x ]

rmCharsRec :: String -> String -> String
rmCharsRec _ [] = []
rmCharsRec s1 (h:t)
    | h `elem` s1 = rmCharsRec s1 t
    | otherwise = h : rmCharsRec s1 t

test_rmchars :: Bool
test_rmchars = rmCharsRec ['a'..'l'] "fotbal" == "ot"

rmCharsFold :: String -> String -> String
rmCharsFold l1 l2 = foldr rmChar l2 l1
    