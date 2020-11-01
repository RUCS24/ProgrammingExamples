// Pig Latin:
// To translate a word from English to Pig Latin, move all of the consonants
// at the beginning of the word to the end, and add -ay. If the word starts
// with a vowel, add -yay without changing anything else. Write a program
// that converts the user input from English to Pig Latin. Keep capitalization
// the same and ignore punctuation.

open System

// Identify whether the character c is a consonant
// by converting it to its lower-case equivalent,
// then pattern matching it with 'a', 'e', 'i', 'o',
// or 'u'. true is returned if any of those patterns
// are matched, and any other patterns return false.
let isConsonant c =
    Char.ToLower(c)
    |>  function
        | 'a' | 'e' | 'i' | 'o' | 'u' -> false
        | _ -> true

// Given a predicate function p and a list l,
// return a tuple wherein the first value contains
// the longest continuous block of elements in l
// from the beginning that satisfy the predicate p,
// and the second value contains the remaining elements
// of l
let rec span p l =
    match l with
    | [] -> (l, l) // An empty list for l should just return a pair of empty lists
    // Split l into its head (first element) and its tail (remaining elements)
    // if and only if the predicate function returns true when applied to the head
    | h :: t when p h -> 
        // Recursively apply span to the tail
        // and save its results in a tuple (a, b)
        let (a, b) = span p t
        (h :: a, b) // Prepend the head of l to a; b is the remaining elements of l
    // If the predicate is not satisfied by the head,
    // the list of initial elements satisfying the
    // predicate is empty, and the remaining elements
    // are simply l
    | _ -> ([], l) 

// Apply a function f to the values of a tuple (x, y)
let tupleMap f (x, y) = (f x, f y)

let piglatin s =
    let (initialConsonants, remainingLetters) =
        s
        |> Seq.toList // Convert the string to a char list
        |> span isConsonant // Create a tuple of initial consonants and remaining letters
        |> tupleMap String.Concat // Turn the tuple values from char lists into strings

    if Seq.isEmpty initialConsonants then
        // No initial consonants, so s + yay
        s + yay 
    else
        // Remaining letters come first, then initial consonants, then "ay"
        sprintf remainingLetters + initialConsonants + "ay"

fsi.CommandLineArgs
|> Seq.skip 1 // Ignore the filename
|> Seq.map piglatin // Apply the piglatin function to each argument
|> String.concat " " // Join them together with spaces
|> printfn "%s" // Print out the result
