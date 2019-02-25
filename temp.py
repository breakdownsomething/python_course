def gcd(a, b):
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert (a>=1 and b>=1)
    while b:
        a, b = b, a % b
    return a
