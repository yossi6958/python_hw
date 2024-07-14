def get_digit(number, m):
    return (number // 10 ** (m - 1)) % 10


def merge(left, right, key_func):
    result = []
    while left and right:
        if key_func(left[0]) <= key_func(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result


def recursive_sort(numbers, key_func):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left = recursive_sort(numbers[:mid], key_func)
    right = recursive_sort(numbers[mid:], key_func)
    return merge(left, right, key_func)


def main_sort(numbers, m):
    sorted_by_digit = recursive_sort(numbers, lambda x: get_digit(x, m))
    fully_sorted = recursive_sort(sorted_by_digit, lambda x: x)
    return sorted_by_digit, fully_sorted


def main():
    numbers = [123, 231, 4323, 4124, 232, 231, 22]
    m = 3
    sorted_numbers_by_digit, fully_sorted_numbers = main_sort(numbers, m)
    print(f"sorted_numbers_by_digit: {sorted_numbers_by_digit}.")
    print(f"fully_sorted_numbers: {fully_sorted_numbers}.")


if __name__ == '__main__':
    main()
