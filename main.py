import pandas as pd

df = pd.read_csv('new.csv')

difficulty_lvl = int(input())

prices = df['price'].values
dates = df['date'].values


def calc_diff_with_first_min(sample):
    purchase_price = min(sample)
    index_of_purchase = list(sample).index(purchase_price)

    sell_price = purchase_price
    index_of_sell = 0

    if index_of_purchase == len(sample):
        sell_price = max(sample[index_of_purchase:])
        index_of_sell = list(sample).index(sell_price)

    return [sell_price - purchase_price, index_of_purchase, index_of_sell]


def calc_diff_with_first_max(sample):
    sell_price = max(sample)
    index_of_sell = list(sample).index(sell_price)

    purchase_price = sell_price
    index_of_purchase = 0

    if index_of_sell != 0:
        purchase_price = min(sample[0:index_of_sell])
        index_of_purchase = list(sample).index(purchase_price)

    return [sell_price - purchase_price, index_of_purchase, index_of_sell]


def get_profit(sample):
    after_max = calc_diff_with_first_max(sample)
    after_min = calc_diff_with_first_min(sample)

    best_profit = after_max if after_max[0] > after_min[0] else after_min

    return best_profit


if difficulty_lvl == 1:
    profit = get_profit(prices)

    print(f'Profit = {profit[0]}')
    print(f'Date of purchase: {dates[profit[1]]}')
    print(f'Date of sell: {dates[profit[2]]}')
elif difficulty_lvl == 2:
    max_p = 0
    steps = []
    for i in range(len(prices) - 1):
        print(f'i = {i}')
        for j in range(i + 1, len(prices) - 2):

            first_operation = get_profit(prices[i:j + 1])
            second_operation = get_profit(prices[j + 1:])
            sum_ = first_operation[0] + second_operation[0]

            max_p = max(sum_, max_p)

            if sum_ >= max_p:
                steps = [dates[first_operation[1]],
                         dates[first_operation[2]],
                         dates[second_operation[1]],
                         dates[second_operation[2]]]

    print(max_p)
    print(steps)
