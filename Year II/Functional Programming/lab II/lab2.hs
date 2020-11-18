import Data.List
import Data.Char

fibonacciCazuri :: Integer -> Integer
fibonacciCazuri n 
    | n < 2 = n
    | otherwise = fibonacciCazuri(n-1) + fibonacciCazuri(n-2)

fibonacciEcuational :: Integer -> Integer
fibonacciEcuational 0 = 0
fibonacciEcuational 1 = 1
fibonacciEcuational n =
    fibonacciEcuational (n-1) + fibonacciEcuational (n-2)

--2.1

fibonacciLiniar :: Integer -> Integer
fibonacciLiniar 0 = 0
fibonacciLiniar n = snd (fibonacciPereche n)
    where
        fibonacciPereche :: Integer -> (Integer, Integer)
        fibonacciPereche 1 = (0, 1)
        fibonacciPereche n = (right, right+left)
            where
                (left, right) = fibonacciPereche(n-1)

semiPareRecDest :: [Int] -> [Int]
semiPareRecDest l
    | null l = l
    | even h = h `div` 2 : t'
    | otherwise = t'
    where
        h = head l
        t = tail l
        t' = semiPareRecDest t

semiPareRecEq :: [Int] -> [Int]
semiPareRecEq [] = []
semiPareRecEq (h:t)
    | even h = h `div` 2 :t'
    | otherwise = t'
    where t' = semiPareRecEq t

semiPareComp :: [Int] -> [Int]
semiPareComp l = [x `div` 2 | x <- l, even x]

--2.2

inIntervalRec :: Int -> Int -> [Int] -> [Int]
inIntervalRec _ _ [] = []
inIntervalRec lo hi (h:t) 
    | h>=lo && h<=hi = h : t'
    | otherwise = t'
    where 
        t' = inIntervalRec lo hi t
    
inIntervalComp :: Int -> Int -> [Int] -> [Int]
inIntervalComp lo hi xs =  [x |  x <- xs, x<=hi, x>=lo]

--2.3

pozitiveRec :: [Int] -> Int
pozitiveRec [] = 0
pozitiveRec (h:t)
    | h > 0 = 1 + t'
    | otherwise = t'
    where
        t' = pozitiveRec t 

pozitiveComp :: [Int] -> Int
pozitiveComp l = length [x | x<-l, x>0]

--2.4

pozitiiImpareRec :: [Int] -> [Int]
pozitiiImpareRec l = aux (zip l [0,1..])
    where
        aux :: [(Int, Int)] -> [Int]
        aux [] = []
        aux (h:t)
            | odd (fst h) = snd h : aux t
            | otherwise = aux t
    
pozitiiImpareComp :: [Int] -> [Int]
pozitiiImpareComp l = [snd(x) | x<-zip l [0,1..], odd(fst x)]

--2.5

multDigitsRec :: String -> Int
multDigitsRec "" = 1
multDigitsRec (h:t)
    | isDigit h = digitToInt h * t'
    | otherwise = t'
    where t' = multDigitsRec t

multDigitsComp :: String -> Int
multDigitsComp l = product [digitToInt x | x<-l, isDigit x]

--2.6

discountRec :: [Float] -> [Float]
discountRec [] = []
discountRec (h:t)
    | 0.75*h < 200 = 0.75*h : l'
    | otherwise = l'
    where l' = discountRec t

discountComp :: [Float] -> [Float]
discountComp l = [0.75*x | x<-l, 0.75*x < 200] 