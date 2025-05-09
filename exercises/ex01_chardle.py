"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730620941"
word : str = input("Enter a 5-character word: ")
if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
letter : str = input("Enter a single character: ")
if len(letter) > 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + letter + " in " + word)
var : int = 0
sam = "s"
if(word[0] == letter):
    print( letter + " found at index 0")
    var = var+1
if(word[1] == letter):
    print( letter + " found at index 1")
    var = var+1
if(word[2] == letter):
    print( letter + " found at index 2")
    var = var+1
if(word[3] == letter):
    print( letter + " found at index 3")
    var = var+1
if(word[4] == letter):
    print( letter + " found at index 4")
    var = var+1
if var == 0:
    var = "No"
if var == 1:
    sam = ""
print( str(var) + " instance" + sam + " of " + letter + " found in " + word)