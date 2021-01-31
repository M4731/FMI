import Test.QuickCheck
import Data.Char ( toUpper )
import Test.QuickCheck.Gen ( Gen(MkGen, unGen) ) 

--1

double :: Int -> Int
double x = 2*x

triple :: Int -> Int
triple x = 3*x

penta :: Int -> Int
penta x = 5*x
 
test :: Int -> Bool
test x = (double x + triple x) == (penta x)

test2 :: Int -> Bool
test2 x = (double x + triple x) == (penta x) + x

--2

myLookUp :: Int -> [(Int,String)]-> Maybe String
myLookUp x [] = Nothing
myLookUp x (h:t) 
     | x == fst h = Just (snd h)
     | otherwise = myLookUp x t

testLookUp :: Int -> [(Int,String)] -> Bool
testLookUp x l = myLookUp x l == lookup x l

testLookUpCond :: Int -> [(Int,String)] -> Property
testLookUpCond n list = n > 0 && n `div` 5 == 0 ==> testLookUp n list

--3

myLookUp' :: Int -> [(Int,String)]-> Maybe String
myLookUp' x [] = Nothing
myLookUp' x ((n, sir):t) 
     | x == n && sir == "" = Just ""
     | x == n = let p:ps = sir in Just (toUpper p : ps)
     | otherwise = myLookUp' x t

capitalized :: [Char] -> [Char]
capitalized (h:t) = toUpper h : t
capitalized [] = "" 

testLookUp' :: Int -> [(Int,String)] -> Bool
testLookUp' x l = myLookUp' x l == lookup x l

testy2Cond :: Int -> [(Int,String)]-> Property
testy2Cond n list = foldr (&&) True (map (\x -> capitalized (snd x) == snd x) list) ==> testLookUp' n list

--4

data ElemIS = I Int | S String
     deriving (Show,Eq)

instance Arbitrary ElemIS where
     arbitrary = oneof [geni, gens]
               where
                    f = unGen (arbitrary :: Gen Int)
                    g = unGen (arbitrary :: Gen String)
                    geni = MkGen (\s i -> let x = f s i in I x)
                    gens = MkGen (\s i -> let x = g s i in S x)

--sau

-- instance Arbitrary ElemIS where
--      arbitrary = do
--           i <- arbitrary
--           s <- arbitrary
--           elements [I i, S s]


myLookUpElem :: Int -> [(Int,ElemIS)]-> Maybe ElemIS
myLookUpElem x [] = Nothing
myLookUpElem x (h:t) 
     | x == fst h = Just (snd h) 
     | otherwise = myLookUpElem x t


testLookUpElem :: Int -> [(Int,ElemIS)] -> Bool
testLookUpElem x l = myLookUpElem x l == lookup x l