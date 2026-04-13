from dic_morse import NESTED_MORSE
import sys


def convert_to_morse(msg: str) -> str:
    morse_msg = []
    for char in msg:
        if char.upper() in NESTED_MORSE:
            morse_msg.append(NESTED_MORSE[char.upper()].strip())
        else:
            raise AssertionError("the arguments are bad")
    return " ".join(morse_msg)

def main():
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    morse_msg = convert_to_morse(str(sys.argv[1]))
    print(morse_msg)

if __name__ == "__main__":
    try:
        main()
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
