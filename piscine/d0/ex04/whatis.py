import sys

def even_or_odd(number: int) -> str:
    if(number % 2 == 0):
        return ("Even")
    else:
        return ("Odd")

try:
    assert len(sys.argv) > 1 and len(sys.argv) < 3, "more than one argument is provided"
    assert sys.argv[1].lstrip("-").isnumeric() , "argument is not an integer"
    number = int(sys.argv[1])
    myresult = even_or_odd(number)
    print(f"I'm {myresult}.")
except AssertionError as e:
    print(f"AssertionError: {e}")
