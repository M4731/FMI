data Choice
    = Rock
    | Paper
    | Scrissors
    deriving(Eq, Show)

data Result
    = Win
    | Loss
    | Draw
    deriving(Eq, Show)

game :: Choice -> Choice -> Result
game a b =
    if a == Rock && b == Scrissors || a == Scrissors && b == Paper || a == Paper && b == Rock
        then Win
    else if a == b
        then Draw
    else Loss
