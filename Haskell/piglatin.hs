import Data.Char
-- Returns true if the character c is not
-- 'a', 'e', 'i', 'o', or 'u' when made lower-case
isConsonant :: Char -> Bool
isConsonant c = (toLower c) `notElem` ['a', 'e', 'i', 'o', 'u']

piglatin :: String -> String
-- Split the string s into a tuple of strings,
-- where the former contains the initial consonants
-- and the latter contains the remaining letters
piglatin s = case (span isConsonant s) of
                -- If no initial consonants,
                -- remaining letters ++ "yay"
                ([], word)  -> word ++ "yay"
                -- If initial consonants,
                -- remaining letters ++ initial consonants
                -- ++ "ay"
                (ic, rl)    -> rl ++ ic ++ "ay"

main = do
    -- Get a line of input from stdin
    input <- getLine
    -- split the input into words, map piglatin to
    -- each word, rejoin them with spaces, and print
    -- out the resulting string
    print . unwords . map piglatin . words $ input
