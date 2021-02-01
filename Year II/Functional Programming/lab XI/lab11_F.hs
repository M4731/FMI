{-# LANGUAGE FlexibleInstances #-}
import Data.Monoid
import Data.Semigroup (Max (..), Min (..))
import Data.Foldable (foldMap, foldr)
import Data.Char (isUpper)

--FOLDABLE

--1

elem :: (Foldable t, Eq a) => a -> t a -> Bool
elem x = foldr (\a b -> b || a == x) False

null :: (Foldable t) => t a -> Bool
null = foldr (\a b -> False) True

length :: (Foldable t) => t a -> Int
length = foldr (\a b -> b + 1) 0

toList :: (Foldable t) => t a -> [a]
toList = foldMap (:[])

fold :: (Foldable t, Monoid m) => t m -> m
fold = foldMap (id) 

--2

data Constant a b = Constant b
instance Foldable (Constant a) 
  where foldMap f (Constant x) = f x

data Two a b = Two a b
instance Foldable (Two a)
  where foldMap f (Two _ b) = f b

data Three a b c = Three a b c
instance Foldable (Three a b)
  where foldMap f (Three _ _ c) = f c

data Three' a b = Three' a b b
instance Foldable (Three' a)
  where foldMap f (Three' a b1 b2) = f b1 <> f b2

data Four' a b = Four' a b b b
instance Foldable (Four' a)
  where foldMap f (Four' a b1 b2 b3) = f b1 <> f b2 <> f b3

data GoatLord a = NoGoat | OneGoat a | MoreGoats (GoatLord a) (GoatLord a) (GoatLord a)
instance Foldable GoatLord where
  foldMap f = go
    where
      go NoGoat = mempty
      go (OneGoat a) = f a
      go (MoreGoats a b c) = go a <> go b <> go c

--3

filterF
     :: ( Applicative f
        , Foldable t
        , Monoid (f a)
        )
     => (a -> Bool) -> t a -> f a
filterF f = foldMap select
  where
    select a
      | f a       = pure a
      | otherwise = mempty

unit_testFilterF1 :: Bool
unit_testFilterF1 = filterF Data.Char.isUpper "aNA aRe mEre" == "NARE"
unit_testFilterF2 :: Bool
unit_testFilterF2 = filterF Data.Char.isUpper "aNA aRe mEre" == First (Just 'N')
unit_testFilterF3 :: Bool
unit_testFilterF3 = filterF Data.Char.isUpper "aNA aRe mEre" == Min 'A'
unit_testFilterF4 :: Bool
unit_testFilterF4 = filterF Data.Char.isUpper "aNA aRe mEre" == Max 'R'
unit_testFilterF5 :: Bool
unit_testFilterF5 = filterF Data.Char.isUpper "aNA aRe mEre" == Last (Just 'E')


--FUNCTOR

--1

newtype Identity a = Identity a
instance Functor Identity
  where fmap f (Identity a) = Identity (f a) 
 
data Pair a = Pair a a
instance Functor Pair
  where fmap f (Pair a1 a2) = Pair (f a1) (f a2)
 
instance Functor (Two a) 
  where fmap f (Two a b) = Two a (f b)
 
instance Functor (Three a b)
  where fmap f (Three a b c) = Three a b (f c)
 
instance Functor (Three' a)
  where fmap f (Three' a b1 b2) = Three' a (f b1) (f b2)
 
data Four a b c d = Four a b c d
instance Functor (Four a b c)
  where fmap f (Four a b c d) = Four a b c (f d)
 
data Four'' a b = Four'' a a a b
instance Functor (Four'' a)
  where fmap f (Four'' a1 a2 a3 b) = Four'' a1 a2 a3 (f b)
 
instance Functor (Constant a)
  where fmap f (Constant b) = Constant (f b)

data Quant a b = Finance | Desk a | Bloor b
instance Functor (Quant a) where 
  fmap f (Finance) = Finance
  fmap f (Desk a) = Desk a
  fmap f (Bloor b) = Bloor (f b)
 
data K a b = K a
instance Functor (K a)
  where fmap f (K a) = K a
 
newtype Flip f a b = Flip (f b a) deriving (Eq, Show)
  -- pentru Flip nu trebuie să faceți instanță

instance Functor (Flip K a) where
  fmap f (Flip (K b)) = Flip (K (f b))  
 
data LiftItOut f a = LiftItOut (f a)
instance Functor f => Functor (LiftItOut f) where
  fmap f (LiftItOut fa) = LiftItOut (fmap f fa)
 
data Parappa f g a = DaWrappa (f a) (g a)
instance (Functor f, Functor g) => Functor (Parappa f g) where
  fmap f (DaWrappa a b) = DaWrappa (fmap f a) (fmap f b)
 
data IgnoreOne f g a b = IgnoringSomething (f a) (g b)
instance Functor g => Functor (IgnoreOne f g a) where
  fmap f (IgnoringSomething x y) = IgnoringSomething x (fmap f y)
 
data Notorious g o a t = Notorious (g o) (g a) (g t)
instance Functor g => Functor (Notorious g o a) where
  fmap f (Notorious x y z) = Notorious x y (fmap f z)
 
instance Functor GoatLord where
  fmap f (NoGoat) = NoGoat
  fmap f (OneGoat a) = OneGoat (f a)
  fmap f (MoreGoats a b c) = MoreGoats (fmap f a) (fmap f b) (fmap f c)
 
data TalkToMe a = Halt | Print String a | Read (String -> a)
instance Functor TalkToMe where
  fmap f (Halt) = Halt
  fmap f (Print x a) = Print x (f a)
  fmap f (Read g) = Read (f . g)