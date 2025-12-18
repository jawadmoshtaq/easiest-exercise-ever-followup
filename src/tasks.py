def task01_countdown(n: int) -> None:
    """Print numbers from n down to 1 using a loop."""
    if n <= 0:
        return
    while n >= 1:
        print(n)
        n -= 1
