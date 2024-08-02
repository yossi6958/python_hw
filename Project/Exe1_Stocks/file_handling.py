import csv

from Project.Exe1_Stocks.profit_logic import get_all_dates


class GetPricesError(Exception):
    pass


def get_prices(filename):
    dates = []
    prices = []

    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                try:
                    date = row[0]
                    price = float(row[1])

                    dates.append(date)
                    prices.append(price)

                except ValueError as e:
                    print(f"ValueError encountered: {e}. Skipping row: {row}")
    except FileNotFoundError as e:
        raise GetPricesError(f"The file '{filename}' was not found.") from e
    except IOError as e:
        raise GetPricesError(f"An IOError occurred while reading '{filename}'. Details: {e}") from e

    return dates, prices


def write_transactions(infile, outfile):
    try:
        dates, prices = get_prices(infile)
    except GetPricesError as e:
        print(f"Error in get_prices function: {e}")
        return 0
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return 0

    total_profit = 0
    num_sells = 0

    try:
        transactions = get_all_dates(prices)

        with open(outfile, mode='w') as file:
            for buy_day, sell_day in transactions:
                file.write(f"Buy: {dates[buy_day]}\n")
                file.write(f"Sell: {dates[sell_day]}\n")

                profit = prices[sell_day] - prices[buy_day]
                total_profit += profit
                num_sells += 1

        print(f"Number of sell days: {num_sells}")

    except FileNotFoundError as e:
        print(f"Error: The file '{outfile}' was not found.")
        return 0
    except IOError as e:
        print(f"Error: An IOError occurred while writing '{outfile}'. Details: {e}")
        return 0
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return 0

    return total_profit
