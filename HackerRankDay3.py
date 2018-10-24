#Name: HackerRankDay3.py
#purpose: Practicing conditional statements
#Author: Trevor Whitley
#Date: 10/24/18

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    if N % 2 != 0:
        print('Weird')
    elif N % 2 == 0:
        if N < 5:
            print('Not Weird')
        elif N <= 20: 
            print('Weird')
        elif N > 20:
            print('Not Weird')
