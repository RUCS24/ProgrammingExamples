open System

let isConsonant = function
    | 'a' | 'e' | 'i' | 'o' | 'u' -> false
    | _ -> true

let rec span p l =
    match l with
    | [] -> (l, l)
    | h :: t when p h ->
        let (a, b) = span p t
        (h :: a, b)
    | _ -> ([], l)

let tupleMap f (x, y) = (f x, f y)

let piglatin s =
    let (initialConsonants, remainingLetters) =
        s
        |> Seq.toList
        |> span isConsonant
        |> tupleMap String.Concat

    if Seq.isEmpty initialConsonants then
        sprintf "%syay" s
    else
        sprintf "%s%say" remainingLetters initialConsonants

fsi.CommandLineArgs
|> Seq.skip 1
|> Seq.map piglatin
|> String.concat " "
|> printfn "%s"
