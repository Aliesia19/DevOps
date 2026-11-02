
from string_utils import print_string, check_case
from generators import parity_generator

def main():
    print("Завдання 1")
    print_string("Independent Work 2")
    print_string(123)

    print("\nЗавдання 2")
    check_case("HELLO")
    check_case("hello")
    check_case("Hello")
    check_case(123)

    print("\nЗавдання 3")
    word = "smogtether"
    letters = list(word.upper())
    print(letters)

    print("\nЗавдання 4")
    generator = parity_generator()

    for _ in range(6):
        print(next(generator))


if __name__ == "__main__":
    main()
