data Expr = Const Int -- integer constant
          | Expr :+: Expr -- addition
          | Expr :*: Expr -- multiplication
           deriving Eq
data Operation = Add | Mult deriving (Eq, Show)

data Tree = Lf Int -- leaf
          | Node Operation Tree Tree -- branch
           deriving (Eq, Show)
           

--1

--a

instance Show Expr where
     show(Const s) = show s
     show(s :+: q) = "(" ++ show s ++ "+" ++ show q ++ ")"
     show(s :*: q) = "(" ++ show s ++ "*" ++ show q ++ ")"

--b

evalExp :: Expr -> Int
evalExp (Const x) = x
evalExp (s :+: q) = evalExp s + evalExp q
evalExp (s :*: q) = evalExp s * evalExp q

exp1 :: Expr
exp1 = (Const 2 :*: Const 3) :+: (Const 0 :*: Const 5)
exp2 :: Expr
exp2 = Const 2 :*: (Const 3 :+: Const 4)
exp3 :: Expr
exp3 = Const 4 :+: (Const 3 :*: Const 3)
exp4 :: Expr
exp4 = ((Const 1 :*: Const 2) :*: (Const 3 :+: Const 1)) :*: Const 2

test11 :: Bool
test11 = evalExp exp1 == 6
test12 :: Bool
test12 = evalExp exp2 == 14
test13 :: Bool
test13 = evalExp exp3 == 13
test14 :: Bool
test14 = evalExp exp4 == 16

--c

evalArb :: Tree -> Int
evalArb (Lf x) = x
evalArb (Node Add t1 t2) = evalArb t1 + evalArb t2
evalArb (Node Mult t1 t2) = evalArb t1 * evalArb t2

--d

expToArb :: Expr -> Tree
expToArb (Const x) = Lf x
expToArb (s :+: q) = Node Add (expToArb s) (expToArb q)
expToArb (s :*: q) = Node Mult (expToArb s) (expToArb q)

arb1 :: Tree
arb1 = Node Add (Node Mult (Lf 2) (Lf 3)) (Node Mult (Lf 0)(Lf 5))
arb2 :: Tree
arb2 = Node Mult (Lf 2) (Node Add (Lf 3)(Lf 4))
arb3 :: Tree
arb3 = Node Add (Lf 4) (Node Mult (Lf 3)(Lf 3))
arb4 :: Tree
arb4 = Node Mult (Node Mult (Node Mult (Lf 1) (Lf 2)) (Node Add (Lf 3)(Lf 1))) (Lf 2)

test21 :: Bool
test21 = evalArb arb1 == 6
test22 :: Bool
test22 = evalArb arb2 == 14
test23 :: Bool
test23 = evalArb arb3 == 13
test24 :: Bool
test24 = evalArb arb4 == 16

--e  

class MySmallCheck a where
     smallValues :: [a]
     smallCheck :: ( a -> Bool ) -> Bool
     smallCheck prop = and [ prop x | x <- smallValues ]

--f

instance MySmallCheck Expr where 
    smallValues = [exp1, exp2, exp3, exp4]

checkExp :: Expr -> Bool
checkExp exp = evalExp exp == evalArb (expToArb exp)

checksmall :: Bool
checksmall = smallCheck checkExp 




