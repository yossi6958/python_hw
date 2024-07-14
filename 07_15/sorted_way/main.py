def get_digit(number, m):
    return (number // 10 ** (m - 1)) % 10


def sort_by_mth_digit(numbers, m):
    return sorted(numbers, key=lambda x: get_digit(x, m))


def main_sort(numbers, m):
    sorted_by_digit = sort_by_mth_digit(numbers, m)
    fully_sorted = sorted(sorted_by_digit)
    return sorted_by_digit, fully_sorted


def main():
    numbers = [123, 231, 4323, 4124, 232, 231, 22]
    m = 1
    sorted_by_digit, fully_sorted = main_sort(numbers, m)
    print(f"sorted_by_digit: {sorted_by_digit}.")
    print(f"fully_sorted: {fully_sorted}.")


if __name__ == '__main__':
    main()
