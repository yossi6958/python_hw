def get_buy_sell_dates(price_list):
    """
    returns the best pair of buy and sell dates to maximize profit.
    :param price_list:
    :return: None if no profit pair exists, a pair of buy day, sell day, if there is one.
    """
    min_price = price_list[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(len(price_list)):
        if price_list[i] < min_price:
            min_price = price_list[i]
            buy_day = i

        current_profit = price_list[i] - min_price
        if current_profit > max_profit:
            max_profit = current_profit
            sell_day = i

    if max_profit == 0:
        return None

    return buy_day, sell_day


def get_all_dates(price_list):
    """
    returns a list of transactions that gain the most profit.
    :param price_list:
    :return: transactions: list of (buy, sell) pairs.
    """
    n = len(price_list)
    if n < 2:
        return []

    transactions = []
    i = 0

    while i < n - 1:
        while i < n - 1 and price_list[i] >= price_list[i + 1]:
            i += 1
        if i == n - 1:
            break
        buy_day = i
        i += 1

        while i < n and price_list[i] >= price_list[i - 1]:
            i += 1
        sell_day = i - 1

        transactions.append((buy_day, sell_day))

    return transactions

