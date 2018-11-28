'''
Created on 26 September 2018
@author:   jcheng15
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 4
'''

"""Takes a list of items with weights and values, and calculates the maximum possible weights and values given
capacity"""

def knapsack(capacity, itemList):
    if capacity == 0 or itemList == []:
        return [0, []]
    if itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    useit = knapsack(capacity - itemList[0][0], itemList[1:])
    loseit = knapsack(capacity, itemList[1:])
    if (useit[0] + itemList[0][1]) > loseit[0]:
        return [useit[0] + itemList[0][1], [itemList[0]]+ useit[1]]
    return loseit


print(knapsack(24, [[36, 35], [10, 28], [39, 47], [8, 1], [7, 24]]), [52, [[10, 28], [7, 24]]])

