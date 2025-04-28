import math
from functools import reduce

def max_valid_divisor(arr_src, arr_other):
    # 1) gcd of source array
    g = reduce(math.gcd, arr_src)
    if g <= 1:
        return 0

    # 2) collect all divisors of g
    divs = []
    root = int(math.isqrt(g))
    for i in range(1, root + 1):
        if g % i == 0:
            divs.append(i)
            if i != g // i:
                divs.append(g // i)

    # 3) test from largest to smallest (skip 1)
    for d in sorted(divs, reverse=True):
        if d == 1:
            continue
        # if d divides none in the other array, it's valid
        if all(x % d != 0 for x in arr_other):
            return d
    return 0

def solution(arrayA, arrayB):
    # candidate from A against B, and B against A
    res1 = max_valid_divisor(arrayA, arrayB)
    res2 = max_valid_divisor(arrayB, arrayA)
    return max(res1, res2)
