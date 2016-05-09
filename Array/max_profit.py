# Quesiton: You are given the stock prices for a set of days . Each day, you can either buy one unit of stock, sell any number of stock units you have already bought, or do nothing. What is the maximum profit you can obtain by planning your trading strategy optimally.

def maxProfit(array):
    # array = [1,10,12,13,9,4]
    max_profit = 0
    curr_profit = 0
    temp_buy = 0
    buy = 0
    sell = 0
    for i in range(1,len(array)):
        curr = array[i] - array[temp_buy]
        if curr > curr_profit:
            curr_profit = curr
        else:
            temp_buy = i
            curr_profit = 0
        if curr_profit > max_profit:
            max_profit = curr_profit
            buy = temp_buy
            sell = i
    return max_profit, buy, sell
