#!/usr/bin/python3

"""Write a Python program to calculate the maximum profit 
from selling and buying values of stock. An array of numbers represent 
the stock prices in chronological order.
For example, given [8, 10, 7, 5, 7, 15], the function will return 10, 
since the buying value of the stock is 5 dollars and sell value is 15 dollars.
Sample Input:
([8, 10, 7, 5, 7, 15])
([1, 2, 8, 1])
([])
Sample Output:
10
7
0"""

# Time Complexity: O(n^2)
# def maxProfit(list):
#     max_profit = 0
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[j] - list[i] > max_profit:
#                 max_profit = list[j] - list[i]
#     return max_profit 

# Time Complexity: O(n)
def maxProfit(list):
    max_profit, current_max = 0,0
    for price in reversed(list):
        current_max = max(current_max,price)
        possible_profit = current_max - price
        max_profit = max(possible_profit,max_profit)
    return max_profit

if __name__ == "__main__":
    print(maxProfit([8, 10, 7, 5, 7, 15]))
    print(maxProfit([1, 2, 8, 1]))
    print(maxProfit([]))
    