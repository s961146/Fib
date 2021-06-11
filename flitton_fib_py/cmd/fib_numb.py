import sys
from typing import Any

from ..fib_calcs.fib_number import recurring_fibonacci_number


def fib_numb() -> None:
    if len(sys.argv) <= 1:
        raise EnvironmentError("You need to input a number to be calculated")
    number: Any = sys.argv[-1]
    try:
        number: int = int(number)
    except ValueError:
        raise EnvironmentError("You need to input an integer")
    print(f"Your Fibonacci number is: {recurring_fibonacci_number(number=number)}")
