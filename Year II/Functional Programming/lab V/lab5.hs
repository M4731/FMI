import Numeric.Natural

--I

logistic :: Num a => a -> a -> Natural -> a
logistic rate start = f
  where
    f 0 = start
    f n = rate * f (n - 1) * (1 - f (n - 1))

logistic0 :: Fractional a => Natural -> a
logistic0 = logistic 3.741 0.00079

ex1 :: Natural
ex1 = 0

--2

ex20 :: Fractional a => [a]
ex20 = [1, logistic0 ex1, 3]

ex21 :: Fractional a => a
ex21 = head ex20

ex22 :: Fractional a => a
ex22 = ex20 !! 2

ex23 :: Fractional a => [a]
ex23 = drop 2 ex20

ex24 :: Fractional a => [a]
ex24 = tail ex20

 --3

ex31 :: Natural -> Bool
ex31 x = x < 7 || logistic0 (ex1 + x) > 2

ex32 :: Natural -> Bool
ex32 x = logistic0 (ex1 + x) > 2 || x < 7

ex33 :: Bool
ex33 = ex31 5

ex34 :: Bool
ex34 = ex31 7

ex35 :: Bool
ex35 = ex32 5

ex36 :: Bool
ex36 = ex32 7

--II

--1

sumaPatrateImpare :: [Integer] -> Integer
sumaPatrateImpare [] = 0 
sumaPatrateImpare (h:t) 
    | odd h = h*h + lista
    | otherwise = lista
    where lista = sumaPatrateImpare t

sumaPatrateImpareFold :: [Integer] -> Integer
sumaPatrateImpareFold = foldr op unit 
    where 
    unit = 0
    h `op` suma 
        | odd h = h*h + suma
        | otherwise = suma 

produsFold :: [Integer] -> Integer
produsFold = foldr (*) 1

--2

map_ :: (a->b) -> [a] -> [b]
map_ f [] = []
map_ f (h:t) = f h : map_ f t

mapFold :: (a->b) -> [a] -> [b]
mapFold f = foldr op unit
    where
        unit = []
        a `op` l = f a : l

--3

filter_ :: (a->Bool) -> [a] -> [a] 
filter_ f [] = []
filter_ f (h:t)
    | f h = h : filter_ f t 
    | otherwise = filter_ f t 

filterFold :: (a->Bool) -> [a] -> [a] 
filterFold f = foldr op unit
    where
        unit = []
        h `op` t 
            | f h = h : t 
            | otherwise = t 

--ex 1

semn :: [Integer] -> String
semn [] = ""
semn (h:t)
    | h < 10 && h > 0 = '+' : t'
    | h > -10 && h < 0 = '-' : t'
    | h == 0 = '0' : t'
    | otherwise = t'
    where t' = semn t

test_semn :: Bool 
test_semn = semn[5,10,-5,0] == "+-0"

semnFold :: [Integer] -> String
semnFold = foldr op unit
   where
     unit = []
     h `op` t 
        | h < 10 && h > 0 = '+' : t
        | h > -10 && h < 0 = '-' : t
        | h == 0 = '0' : t
        | otherwise = t
    
test_semn_foldr :: Bool 
test_semn_foldr = semnFold[5,10,-5,0] == "+-0"

--III

--ex 1

matrice :: Num a => [[a]]
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]     

corect :: [[Integer]] -> Bool 
corect [] = True 
corect (h:t)
    | null t = True
    | length h == length (head t) = t'
    | otherwise = False 
    where t' = corect t

--ex 2

el :: [[a]] -> Int -> Int -> a 
el matrice a b = (matrice !! a) !! b

--ex 3

enumera :: [a] -> [(a,Int)]
enumera l = zip l [0..]

insertPoz :: ([(a,Int)],Int) -> [(a,Int,Int)]
insertPoz (l, lin) = 
    map (\(x,col) -> (x,lin,col)) l

transforma :: [[a]] -> [(a, Int, Int)]
transforma matrix = concatMap insertPoz (enumera (map enumera matrix))