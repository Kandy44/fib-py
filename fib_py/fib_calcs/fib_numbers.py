from typing import List, Optional
from .fib_number import iter_fib_number


def calculate_numbers(numbers: List[int]) -> List[Optional[int]]:
    return [iter_fib_number(n=n) for n in numbers]
