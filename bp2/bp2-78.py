#!/usr/bin/python3

"""The price of a given stock on each day is stored in an array.
Write a Python program to find the maximum profit in one transaction 
i.e., buy one and sell one share of the stock from the given price 
value of the said array. You cannot sell a stock before you buy one.
Input (Stock price of each day): [224, 236, 247, 258, 259, 225]
Output: 35
Explanation:
236 - 224 = 12
247 - 224 = 23
258 - 224 = 34
259 - 224 = 35
225 - 224 = 1
247 - 236 = 11
258 - 236 = 22
259 - 236 = 23
225 - 236 = -11
258 - 247 = 11
259 - 247 = 12
225 - 247 = -22
259 - 258 = 1
225 - 258 = -33
225 - 259 = -34"""

# Time Complexity: O(n)
# def maxProfit(list):
#     max_profit, current_max = 0,0
#     for price in reversed(list):
#         current_max = max(current_max,price)
#         possible_profit = current_max - price
#         max_profit = max(max_profit,possible_profit)
#     return max_profit

# Time Complexity: O(n^2)
def maxProfit(list):
    max_profit = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[j] - list[i] > max_profit:
                max_profit = list[j] - list[i]
    return max_profit

if __name__ == "__main__":
    stock_price_of_each_day = [224, 236, 247, 258, 259, 225]
    print(f"Input (Stock price of each day): {stock_price_of_each_day}")
    print(f"Output: {maxProfit(stock_price_of_each_day)}")