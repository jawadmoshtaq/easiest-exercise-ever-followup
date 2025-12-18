from tasks import task01_countdown, task02_is_even, task03_count_until_negative

def main():
    task01_countdown(5)
    print(task02_is_even(10))
    print(task02_is_even(7))

    c = task03_count_until_negative()
    print("Count:", c)

if __name__ == "__main__":
    main()
