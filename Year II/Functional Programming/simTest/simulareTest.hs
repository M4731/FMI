import Numeric.Natural ()
--ex 1

--a

f1a :: Char -> Bool 
f1a a 
    | a `elem` ['a'..'m'] || a `elem` ['A'..'M'] = True
    | a `elem` ['n'..'z'] || a `elem` ['N'..'Z'] = False
    | otherwise = error "eroare"

--b

f1b :: String -> Bool
f1b s = length [x | x <- s, x `elem` ['a'..'m'] || x `elem` ['A'..'M'] ] >  
    length [x | x <- s, x `elem` ['n'..'z'] || x `elem` ['N'..'Z'] ]

--c

aux :: String -> Int
aux "" = 0
aux (h:t)
    | h `elem` ['a'..'m'] || h `elem` ['A'..'M'] = suma+1
    | h `elem` ['n'..'z'] || h `elem` ['N'..'Z'] = suma-1
    | otherwise = suma
    where suma  = aux t  

f1c :: String -> Bool
f1c s 
    | aux s > 0 = True
    | otherwise = False

--ex 2

--a

f2a :: [Int] -> [Int] 
f2a a = [fst x | x<-zip a (tail a), fst x == snd x]

--b

f2b :: [Int] -> [Int]
f2b [] = []
f2b (h:t)
    | null t = []
    | h == head t = h : t'
    | otherwise = t'
    where t' = f2b t

--c

prop_cd :: Bool
prop_cd = f2a[2,2,2,2,1] == f2b[2,2,2,2,1] && f2a[42] == f2b[42] && f2b[3,1,1,3,3,5] == 
    f2a[3,1,1,3,3,5]

--sau

prop_cd_bun :: [Int] -> Bool
prop_cd_bun s = f2a s == f2b s
