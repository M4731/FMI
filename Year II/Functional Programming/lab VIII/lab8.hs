import Data.List (nub)
import Data.Maybe (fromJust)


type Nume = String
data Prop
  = Var Nume
  | F
  | T
  | Not Prop
  | Prop :|: Prop
  | Prop :&: Prop
  | Prop :->: Prop
  | Prop :<->: Prop
  deriving (Eq, Read)
infixr 2 :|:
infixr 3 :&:


--1

-- a. (P ∨ Q) ∧ (P ∧ Q)
p1 :: Prop
p1 = (Var "P" :|: Var "Q") :&: (Var "P" :&: Var "Q")

-- b. (P ∨ Q) ∧ (¬P ∧ ¬Q)
p2 :: Prop
p2 = (Var "P" :|: Var "Q") :&: (Not (Var "P") :&: Not (Var "Q"))

-- c. (P ∧ (Q ∨ R)) ∧ ((¬P ∨ ¬Q) ∧ (¬P ∨ ¬R))
p3 :: Prop
p3 = (Var "P" :&: (Var "Q" :|: Var "R")) :&: ((Not (Var "P") :|: Not (Var "Q")) :&: (Not (Var "P") :|: Not (Var "R")))


--2

instance Show Prop where
  show (Var nume) = nume   
  show F = "False"
  show T = "True"
  show (Not p) = "(" ++ "~" ++ show p ++ ")"
  show (p :|: q) = "(" ++ show p ++ "|" ++ show q ++ ")"
  show (p :&: q) = "(" ++ show p ++ "&" ++ show q ++ ")"
  show (p :->: q) = "(" ++ show p ++ "->" ++ show q ++ ")"
  show (p :<->: q) = "(" ++ show p ++ "<->" ++ show q ++ ")"  

 
test_ShowProp :: Bool
test_ShowProp =
    show (Not (Var "P") :&: Var "Q") == "((~P)&Q)"


--3

type Env = [(Nume, Bool)]

impureLookup :: Eq a => a -> [(a,b)] -> b
impureLookup a = fromJust . lookup a

impl :: Bool -> Bool -> Bool
impl False _ = True
impl _ x = x

echiv :: Bool -> Bool -> Bool
echiv x y = x==y

eval :: Prop -> Env -> Bool
eval (Var q) e = impureLookup q e
eval T _ = True
eval F _ = False
eval (Not q) e = not(eval q e)
eval (q :|: p) e = eval q e || eval p e
eval (q :&: p) e = eval q e && eval p e
eval (q :->: p) e = eval q e `impl` eval p e
eval (q :<->: p) e = eval q e `echiv` eval p e
 

test_eval :: Bool
test_eval = eval  (Var "P" :|: Var "Q") [("P", True), ("Q", False)]

test_eval2 :: Bool
test_eval2 = not(eval  (Var "P" :|: Var "Q") [("P", False), ("Q", False)])


--4

variabile :: Prop -> [Nume]
variabile (Var q) = [q]
variabile (Not q) = nub $ variabile q
variabile (q :|: p) = nub $ variabile q ++ variabile p
variabile (q :&: p) = nub $ variabile q ++ variabile p
variabile (q :->: p) = nub $ variabile q ++ variabile p
variabile (q :<->: p) = nub $ variabile q ++ variabile p
variabile _ = []
 
test_variabile :: Bool
test_variabile =
  variabile (Not (Var "P") :&: Var "Q") == ["P", "Q"]


--5

envs :: [Nume] -> [Env]
envs [] = [[]]
envs (h:t) = [(h,val):rest | val <-[False, True], rest<-envs t]
 
test_envs :: Bool
test_envs = 
    envs ["P", "Q"]
    ==
    [ [ ("P",False)
      , ("Q",False)
      ]
    , [ ("P",False)
      , ("Q",True)
      ]
    , [ ("P",True)
      , ("Q",False)
      ]
    , [ ("P",True)
      , ("Q",True)
      ]
    ]


--6

satisfiabila :: Prop -> Bool
satisfiabila a = foldr (||) False (map (\x -> eval a x) ([x | x <-envs (variabile a)]))
 
test_satisfiabila1 :: Bool
test_satisfiabila1 = satisfiabila (Not (Var "P") :&: Var "Q") 
test_satisfiabila2 :: Bool
test_satisfiabila2 = not(satisfiabila (Not (Var "P") :&: Var "P"))


--7

valida :: Prop -> Bool
valida a = foldr (&&) True (map (\x -> eval a x) ([x | x <-envs (variabile a)]))

test_valida1 :: Bool
test_valida1 = not(valida (Not (Var "P") :&: Var "Q"))
test_valida2 :: Bool
test_valida2 = valida (Not (Var "P") :|: Var "P")


--8

tabelAdevar :: Prop -> String
tabelAdevar p = concat $ map (++ "\n") tabel
     where 
       vars = variabile p 
       afis_prima =  concat $ (map (++ " ") vars) ++ [show p]
       evaluari = envs vars
       aux_af tv = (show tv)++ " "
       afis_evaluare  ev = concat $ (map aux_af [snd p | p <- ev]) ++ [show (eval p ev)]
       tabel = afis_prima : (map afis_evaluare evaluari)