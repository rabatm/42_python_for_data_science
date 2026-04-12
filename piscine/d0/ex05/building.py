import sys
import string
from typing import Callable

def display_results(counts: dict[str, int]) -> None:
    """
    fonction qui affiche le resultats du compte,
    prend un dictionnaire en arg de type :
        counts {
            len : int,
            upper : int,
            lower : int,
            punctuation : int,
            digits : int,
            spaces : int
        }
    """
    print(f"The text contains {counts['len']} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")

def count_characters_display(text: str, callback: Callable[[dict], None]) -> dict[str, int]:
    """
    fonction qui compte chaque type de caracter puis
    appel la ft de dispaly passer en arguement.
    """
    count = {
            "len": len(text),
            "upper" : 0,
            "lower" : 0,
            "punctuation" : 0,
            "digits" : 0,
            "spaces" : 0,
    }
    for char in text:
        if (char.isupper()):
            count["upper"] += 1
        elif (char.islower()):
            count["lower"] += 1 
        elif (char.isdigit()):
            count["digits"] += 1
        elif (char.isspace()):
            count["spaces"] += 1
        elif (char in string.punctuation):
            count["punctuation"] += 1
    callback(count)

def main():
    """
    Script qui prends en arg un str et compte :
        - le nombre de majuscules
        - le nombre de minuscules
        - le nombre de poncutations
        - le nombre d'espace
        - le nombre de chiffres
    prends en argument un str optionel
    si pas d'argument le test est demander
    si trop d'argument affiche more than one argument is provided
    """
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    if(len(sys.argv) < 2):
        print("What is the text to count?")
        text = input()
    else:
        text = sys.argv[1]
        print(f"DEBUG: |{text}|")
    count_characters_display(text, display_results)

if __name__ == "__main__":
    try:
        main()
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
