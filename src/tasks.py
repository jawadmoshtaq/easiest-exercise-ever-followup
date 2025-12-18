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

def task03_count_until_negative() -> int:
    """Ask numbers until a negative number is entered; return how many non-negative numbers were entered."""
    count = 0
    while True:
        value = int(input("Enter a number (negative to stop): "))
        if value < 0:
            break
        count += 1
    return count
def task04_divisible_by_7() -> list[int]:
    """Return all numbers between 1 and 100 divisible by 7."""
    result = []
    for i in range(1, 101):
        if i % 7 == 0:
            result.append(i)
    return result
