import Prelude
import qualified Data.List as List

--2

--a

type Key = Int
type Value = String

class Collection c where
  cempty :: c 
  csingleton :: Key ->  Value -> c 
  cinsert:: Key -> Value -> c  -> c 
  cdelete :: Key -> c  -> c 
  clookup :: Key -> c -> Maybe Value
  ctoList :: c  -> [(Key, Value)]

  ckeys :: c  -> [Key]
  ckeys c = [fst p | p <- ctoList c]

  cvalues :: c  -> [Value] 
  cvalues c = [snd p | p <- ctoList c]

  cfromList :: [(Key,Value)] -> c
  cfromList [] = cempty 
  cfromList ((k, v):kvs) = cinsert k v (cfromList kvs)

--b

newtype  PairList 
  = PairList { getPairList :: [(Key,Value)] }


instance Show PairList where
  show (PairList p) = show p

instance Collection PairList where
  cempty = PairList []
  csingleton k v = PairList [(k, v)]
  cinsert k v (PairList list) = if k `elem` map fst list then PairList list else PairList ((k, v): list) 
  cdelete k (PairList list) = PairList [(key,v) | (key,v) <- list, key /= k] 
  clookup k (PairList list) = lookup k list
  ctoList = getPairList

pairlist :: PairList
pairlist = PairList[(1,"ananas"),(2,"bbb"),(3,"casda")]

--c

data SearchTree 
  = Empty
  | Node
      SearchTree  -- elemente cu cheia mai mica 
      Key                    -- cheia elementului
      (Maybe Value)          -- valoarea elementului
      SearchTree  -- elemente cu cheia mai mare
   deriving Show   

instance Collection SearchTree where
  cempty = Empty
  csingleton k v = Node Empty k (Just v) Empty
  cinsert k v Empty = csingleton k v
  cinsert k v (Node st1 key value st2) 
    | k < key = Node (cinsert k v st1) key value st2
    | k > key = Node st1 k (Just v) (cinsert k v st2)
    | otherwise = Node st1 k (Just v) st2
  clookup k Empty = Nothing 
  clookup k (Node st1 key value st2) 
    | k==key = value
    | k<key = clookup k st1 
    | otherwise = clookup k st2
  cdelete k Empty = Empty
  cdelete k (Node st1 key value st2) 
    | k==key = Node st1 key Nothing st2 
    | k<key = Node (cdelete k st1) key value st2 
    | otherwise = Node st1 key value (cdelete k  st2)
  ctoList Empty = []
  ctoList (Node st1 key value st2) = ctoList st1 ++ kvtolist key value ++ ctoList st2
    where 
      kvtolist k (Just v) = [(k,v)]
      kvtolist _ _ = []

st :: SearchTree
st = Node (Node(Node Empty 1 (Just "a") Empty) 2 (Just "b") Empty) 3 (Just "c") Empty