#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

# def solve(arr,n,ts):
    #recursive      Runtime Error
    # if(n==0 or ts<=0):
    #     return 0
    # elif arr[n-1]<=ts:
    #     return max(arr[n-1]+solve(arr,n,ts-arr[n-1]),solve(arr,n-1,ts))
    # else:
    #     return solve(arr,n-1,ts)
    #memoized       Runtime Error
    # global t
    # key = (n,ts)
    # if(n==0 or ts<=0):
    #     return 0
    # if(k in t):
    #     return t[key]
    # if(arr[n-1]<=ts):
    #     t[key] = max(arr[n-1]+solve(arr,n,ts-arr[n-1]),solve(arr,n-1,ts))
    #     return t[key]
    # t[key] = solve(arr,n-1,ts)
    # return t[key]
    #dp

def unboundedKnapsack(k, arr):
    # Write your code here
    n = len(arr)
    # global t      #For memoised solution
    # t = {}
    t = [[-1 for i in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(k+1):
            if(i==0 or j==0):
                t[i][j]=0
            elif(arr[i-1]<=j):
                t[i][j] = max(arr[i-1]+t[i][j-arr[i-1]],t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for i in range(0,t):
        
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()