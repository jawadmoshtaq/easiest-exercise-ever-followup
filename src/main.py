from tasks import task01_countdown, task02_is_even, task03_count_until_negative
from tasks import task04_divisible_by_7



def main():
    task01_countdown(5)
    print(task02_is_even(10))
    print(task02_is_even(7))

    c = task03_count_until_negative()
    print("Count:", c)
    print(task04_divisible_by_7())


if __name__ == "__main__":
    main()
