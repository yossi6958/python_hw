def shopping():
    prices = {'banana': 10, 'apple': 8, 'bread': 7, 'cheese': 20, 'juice': 15}

    shopping_cart = {'banana': 2, 'apple': 5, 'bread': 3, 'cheese': 1, 'juice': 9, 'chocolate': 2}

    total = 0

    for item, quantity in shopping_cart.items():
        if item not in prices:
            print(f"{item} does not exist in our store!")
            continue
        total += prices[item] * quantity

    print(f"Your total price is: {total} shekels")


def main():
    shopping()


if __name__ == '__main__':
    main()
