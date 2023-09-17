from typing import List
from .fib_number import iter_fib_number


def calculate_numbers(numbers_lst: List[int]) -> List[int]:
    return [iter_fib_number(n) for n in numbers_lst]
