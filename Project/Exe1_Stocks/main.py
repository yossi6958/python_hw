from Project.Exe1_Stocks.file_handling import get_prices, write_transactions
from Project.Exe1_Stocks.profit_logic import get_buy_sell_dates

IN_FILENAME = 'djia.csv'
OUT_FILENAME = 'best_djia.txt'


def test_get_buy_sell_dates():
    dates, prices = get_prices(filename=IN_FILENAME)
    buy_date, sell_date = get_buy_sell_dates(price_list=prices)

    print(f"For maximum profit you should:\nbuy in: {dates[buy_date]}\nsell in: {dates[sell_date]}.")


def test_write_transactions():
    total_profit = write_transactions(infile=IN_FILENAME, outfile=OUT_FILENAME)
    print(f"Total profit: ${total_profit:,.0f}")


def main():
    test_write_transactions()


if __name__ == '__main__':
    main()
