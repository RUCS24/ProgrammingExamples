def pigLatin(words): # Takes in a word to convert to pig latin
    vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u") # Identify all vowels with and without capitalization
    for letter in words: # Checks each letter in a word
        if letter in vowels: # Checks for the first vowel in the word
            words = words + "ay"
            return words
        else:
            words = words[1:len(words)] + words[0:1]
    return words + "ay" # If there is only one character and the for loop doesn't run, return words + "ay"
words = input("Enter a word to convert into pig latin: ").split() # Asks user for input string to convert to pig latin
words = [pigLatin(word) for word in words] # Converts each word into pig latin using the pigLatin method
output_phrase = " ".join(words)
print(output_phrase) # Finally outputs the pig latin phrase