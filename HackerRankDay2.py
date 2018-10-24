#Name: HackerRankDay2
#Purpose: user input tip percent, tax percent, and cost and prints total cost.
#Name: Trevor Whitley
#Date 10/23/18

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(mealCost, tipPercent, taxPercent):
    tipAmount = mealCost * tipPercent / 100
    taxAmount = mealCost * taxPercent / 100
    totalCost = round(mealCost + tipAmount + taxAmount)
    print(int(totalCost))

     
mealCost = float(input())

tipPercent = int(input())

taxPercent = int(input())

solve(mealCost, tipPercent, taxPercent)
