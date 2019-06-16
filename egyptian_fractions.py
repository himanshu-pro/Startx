import sys
from typing import NoReturn, Iterator

from fractions import Fraction
from math import ceil


class UnitFraction(Fraction):
    def __new__(cls, denominator: int):
        return super(UnitFraction, cls).__new__(cls, 1, denominator)


# When the loop ends `frac` is less than `unit`
# The unit_fractions contained in `frac` have to be smaller than `frac`
# Hence unit_fractions contained in `frac` are also smaller than `unit`
# All unit_fractions before `unit` were larger than `unit`
# Hence Uniqueness of terms is ensured
def get_egyptian(frac: Fraction) -> Iterator[UnitFraction]:
    unit = UnitFraction(1)
    while frac >= unit:
        yield unit
        frac -= unit
        unit = UnitFraction(unit.denominator + 1)
    yield from _get_egyptian_proper(frac)


# Getting largest unit fractions repeatedly ensures term uniqueness for proper fractions
def _get_egyptian_proper(frac: Fraction) -> Iterator[UnitFraction]:
    while frac > 0:
        unit = get_largest_unit(frac)
        frac -= unit
        yield unit


# ceil(n/m) is the smallest integer larger than n/m by definition
# Hence 1/ceil(n/m) is the largest unit fraction smaller than 1/(n/m)
# Hence Largest unit fraction for m/n i.e 1/(n/m) is 1/ceil(n/m)
def get_largest_unit(frac: Fraction) -> UnitFraction:
    return UnitFraction(ceil(Fraction(frac.denominator, frac.numerator)))


def print_egyptian(frac_rep: str) -> NoReturn:
    for unit in get_egyptian(Fraction(frac_rep)):
        print(unit)


if __name__ == "__main__":
    print_egyptian(sys.argv[1])
