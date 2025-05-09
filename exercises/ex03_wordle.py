__author__ = "730620941"

def contains_char(w1: str, w2: str) -> bool:
    """Finds if w2 is anywhere in w1"""
    assert len(w2) == 1
    return w2 in w1
    
    
def emojified(word: str, sec: str) -> str:
    var: str = ""
    t: int = 0
    L: int = len(sec)
    W: str = "\U00002B1C"
    G: str = "\U0001F7E9"
    Y: str = "\U0001F7E8"
    assert len(word) == len(sec)
    while t < L:
        if word[t] == sec[t]:
            var = var + G
        else:
            if word[t] in sec:
                var = var + Y
            else:
                var = var + W
        t = t + 1
    return var
def input_guess(num: int) -> str:
    track: str = input(f"Enter a {num} character word: ")
    while len(track) != num:
        track: str = input(f"That wasn't {num} chars! Try again ")
    return track
    
    
def main() -> None:
    """The entrypoint of the program and main game loop."""
    time: int = 1
    final: str = "codes"
    while time <= 6:
        print(f"=== Turn {time}/6 ===")
        guess: str = input_guess(5)
        print(emojified(guess,final))
        if guess == final:
            print(f"You won in {time}/6 turns!")
            time = 6
        time = time + 1
    if time == 7:
        print("X/6 - Sorry, try again tomorrow!")