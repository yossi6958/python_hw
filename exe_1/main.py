def good_morning() -> None:
    name = input("Hello, What is your name? ")
    print(f"Good morning {name}!!")


def sum_values() -> None:
    x = 123456
    king_of = 84848484
    zulu = 297345943273842761
    total = sum(locals().values())
    print(f"Sum is {total}")


def eternal_loop() -> None:
    while True:
        print("After the sun")


if __name__ == "__main__":
    good_morning()
    sum_values()
    eternal_loop()
