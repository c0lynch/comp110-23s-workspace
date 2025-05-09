"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730620941"
SEC: str = "python"
L: int = len(SEC)
W: str = "\U00002B1C"
G: str = "\U0001F7E9"
Y: str = "\U0001F7E8"
word: str = input(f"What is your {L}-letter guess? ")
pat: int = 0
in_game: bool = True
var: str = ""
while in_game and pat < 5:
    if pat == 4:
        in_game = False
    if len(word) == L:
        t = int(0)
        while t < L:
            if word[t] == SEC[t]:
                var = var + G
            else:
                if word[t] in SEC:
                    var = var + Y
                else:
                    var = var + W
            t = t + 1
        print(var)
        in_game = False
    else:
        word = input("Try again")
        pat = pat + 1
if not in_game:
    if pat == 4:
        print("Try again")
    if len(word) == L:
        if word == SEC:
            print("Woo! You got it!")
        else:
            print("Try again")