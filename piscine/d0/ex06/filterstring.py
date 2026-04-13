import sys
from ft_filter import ft_filter

def main():
"""
Programme qui prend en arguement une chaine de caracter, et un integer
et qui retroune un list des mots qui sont plus grand que l'integer
exemple : 
    python filterstring.py'Hello the World' 4
        ['Hello','World']
"""
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        if not isinstance(sys.argv[1], str) or sys.argv[2].isdigit() is False:
            raise AssertionError("the arguments are bad")
        number = int(sys.argv[2])
        words = str(sys.argv[1]).split()
        wordslist = ft_filter(lambda word: len(word) > number, words) 
        print(wordslist)

if __name__ == "__main__":
    try:
        main()
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
