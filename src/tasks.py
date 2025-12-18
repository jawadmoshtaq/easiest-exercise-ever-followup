def task01_countdown(n: int) -> None:
    """Print numbers from n down to 1 using a loop."""
    if n <= 0:
        return
    while n >= 1:
        print(n)
        n -= 1
def task02_is_even(x: int) -> bool:
    """Return True if x is even, else False."""
    return x % 2 == 0
