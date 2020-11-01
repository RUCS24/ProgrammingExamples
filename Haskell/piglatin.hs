isConsonant :: Char -> Bool
isConsonant c = c `notElem` ['a', 'e', 'i', 'o', 'u']

piglatin :: String -> String
piglatin s = case (span isConsonant s) of
                ([], word)  -> word ++ "yay"
                (ic, rl)    -> rl ++ ic ++ "ay"

main = do
    input <- getLine
    print . unwords . map piglatin . words $ input
