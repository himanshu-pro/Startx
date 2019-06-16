import math

from typing import List, Iterable, Sequence
from itertools import product


def join(*it: Iterable[int]) -> int:
    return int(''.join(list(map(str, *it))))


def get_even_pal(arr: List[int]) -> List[int]:
    return list(reversed(arr)) + arr


def get_odd_pal(arr: List[int]) -> List[int]:
    return list(reversed(arr[1:])) + arr


# The last digit is chosen to be non-zero because the first digit is known to non-zero
def get_independent(digits: int) -> Iterable[List[int]]:
    for x, l in product(product(range(0, 10), repeat=digits - 1), range(1, 10)):
        yield [*x, l]


# if the maximum number of digits allowed is odd, say 7,
# the 4 independent digits can't be used to make their even palindrome
# because its length will become 8
def get_all_palindromes(max_digits: int) -> Iterable[int]:
    max_independent_digits = math.ceil(max_digits / 2)
    skip_last_even_pal = max_digits % 2 == 1

    for i in range(1, max_independent_digits + 1):
        for choices in get_independent(i):
            yield join(get_odd_pal(choices))
            if not (i == max_independent_digits and skip_last_even_pal):
                yield join(get_even_pal(choices))


def is_palindrome_in_binary(num: int) -> bool:
    return is_palindrome(bin(num)[2:])


def is_palindrome(seq: Sequence) -> bool:
    return list(reversed(seq)) == list(seq)


if __name__ == '__main__':
    # palindromes less than 1_000_000 means palindromes with 6 digits or less
    print(sum(x for x in get_all_palindromes(6) if is_palindrome_in_binary(x)))
