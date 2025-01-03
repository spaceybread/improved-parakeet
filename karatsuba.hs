-- Split a number into two halves
spn :: Int -> (Int, Int)
spn num = 
    let n = floor (logBase 10 (fromIntegral num)) + 1 
        mid = n `div` 2
        divisor = 10 ^ mid
        fh = num `div` divisor
        sh = num `mod` divisor
    in (fh, sh)

-- Get number of digits
num_dig :: Int -> Int
num_dig n = length (show (abs n))

-- Karatsuba's 
kar :: Int -> Int -> Int
kar n1 n2
    | n1 < 10 || n2 < 10 = n1 * n2
    | otherwise =
        let n = num_dig n1
            mid = n `div` 2
            sn1 = spn n1
            sn2 = spn n2
            a = fst sn1
            b = snd sn1
            c = fst sn2
            d = snd sn2

            ac = kar a c
            bd = kar b d
            x1 = a + b
            x2 = c + d
            ad_bc = (kar x1 x2) - ac - bd
            out = 10^(2 * mid) * ac + 10^mid * ad_bc + bd
        in out

main :: IO ()
main = do
    -- Example
    let a = 12345678 
    let b = 87654321
    let res = kar a b
    print(res)