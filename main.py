import math

def s_operator_ultimate(n):
    """
    Implementation of the S-Operator for Topological Collapse.
    Protected by DOI 10.5281/zenodo.18273451
    """
    x = math.isqrt(n) + 1
    while True:
        y2 = x*x - n
        if y2 < 0:
            x += 1
            continue
        y = math.isqrt(y2)
        if y*y == y2:
            return x - y, x + y # Collapse reached
        x += 1
