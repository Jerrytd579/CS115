# Created on Sep 19, 2018
#
# I pledge my honor that I have abided by the Stevens Honor System.
# @author Jerry Cheng
# jcheng15
#

def change(amount, coins):
    """Given an amount of money, amount, and a list of coin types, coins, calculates the minimum
    number of coins it would take to achieve that coin amount"""
    if amount == 0:
        return 0
    if coins == [] or amount < 0:
        return float("inf")
    useit = 1 + change(amount - coins[0], coins)
    loseit = change(amount, coins[1:])
    return min(useit, loseit)

print(change(48, [1, 5, 10, 25, 50]))
