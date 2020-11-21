--3.1

{-
[x^2 | x <- [1 .. 10], x `rem` 3 == 2]
[(x, y) | x <- [1 .. 5], y <- [x .. (x+2)]]
[(x, y) | x <- [1 .. 3], let k = x^2, y <- [1 .. k]]
[x | x <- "Facultatea de Matematica si Informatica", elem x ['A' .. 'Z']]
[[x .. y] | x <- [1 .. 5], y <- [1 .. 5], x < y ]
-}

factori :: Int -> [Int]
factori n = [w | w<-[1..n], n `rem` w == 0]

prim :: Int -> Bool
prim n = factori n == [1,n]

numerePrime :: Int -> [Int]
numerePrime n = [x | x<-[2..n], prim x]

--3.2

-- L3.2 Testati si sesizati diferenta:
-- [(x,y) | x <- [1..5], y <- [1..3]]
-- zip [1..5] [1..3]

myzip3 :: [Int] -> [Int] -> [Int] -> [(Int, Int, Int)]
myzip3 _ _ [] = []
myzip3 _ [] _ = []
myzip3 [] _ _ = []
myzip3 (h1:t1) (h2:t2) (h3:t3) = 
    (h1,h2,h3) : myzip3 t1 t2 t3

aplica2 :: (a -> a) -> a -> a
aplica2  = \f x -> f (f x)
--aplica2 f x = f (f x)
--aplica2 f = f.f
--aplica2 f = \x -> f (f x)

putere x = x^2
adunare x = x+3

{-
*Main> map (^2) [1..5]
[1,4,9,16,25]
*Main> map (^3) [1..5]
[1,8,27,64,125]
*Main> map (+3) [1..5]
[4,5,6,7,8]
-}
{-
map (\ x -> 2 * x) [1 .. 10]
map (1 `elem` ) [[2, 3], [1, 2]]
map ( `elem` [2, 3] ) [1, 3, 4, 5]
map ($3) [(4+),(10*),(^2),(sqrt)]
-}

--3.3

firstEl l = map fst l
--firstEl [ ('a', 3), ('b', 2), ('c', 1)]

sumList l = map suma l
-- sumList [[1, 3],[2, 4, 5], [], [1, 3, 5, 6]]

suma :: [Int] -> Int
suma [] = 0
suma (h:t) = h + t'
    where t' = suma t

prel :: Integer -> Integer
prel x 
    | even x = x`div` 2
    | otherwise = x* 2

prel2 :: [Integer] -> [Integer]
prel2 x = map prel x
-- prel2 [2,4,5,6]

--3.4

{-
filter (>2) [3,1,4,2]
filter odd [1,2,3,4,5,6]
-}

p341 :: Char -> [String] -> [String]
p341 c l = filter (c `elem`) l

p342 :: [Integer] -> [Integer]
p342 l = map (^2) q
    where q = filter odd l

aux :: (Integer,Integer) -> Bool
aux x = odd(snd x) 

puter3 :: (Integer, Integer) -> Integer
puter3 x = fst x^2

p343 :: [Integer] -> [Integer]
p343 l = map puter3 (filter aux (l `zip` [0..]) )

ajutor l = filter(`elem` "AEIOUaeiou") l

p344 :: [String] -> [String]
p344 l = myMap(ajutor) l

--3.5

myMap :: (a -> b) -> [a] -> [b]
myMap _ [] = []
myMap f (h:t) = 
    f h : t'
    where t' = myMap f t

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter _ [] = []
myFilter f (h:t) 
    | f h = h : myFilter f t
    | otherwise = myFilter f t
