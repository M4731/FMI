import Data.List

myInt = 55555555555555555555555555555555555555555555555555555555555

double :: Integer -> Integer
double x = x + x

triple :: Integer -> Integer
triple x = x + x + x

maxim :: Integer -> Integer -> Integer
maxim x y = if (x > y) then x else y

maxym :: Integer -> Integer -> Integer
maxym x y = 
    if (x > y) 
        then x 
    else y

maxim3 :: Integer -> Integer -> Integer -> Integer
maxim3 x y z =
    if (x > y && x > z)
        then x
    else if (y > x && y > z)
        then y
    else z

maxym3 :: Integer -> Integer -> Integer -> Integer
maxym3 x y z = 
    let 
        u = (maxim x y) 
    in 
        maxim u z 

maxim4 :: Integer -> Integer -> Integer -> Integer -> Integer
maxim4 x y w z =
    let
        u = (maxim3 x y z)
    in
        maxim u w