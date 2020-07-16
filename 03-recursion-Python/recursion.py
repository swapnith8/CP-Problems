"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    x = 0
    y = 1
    if (position < 0):
        return x
    elif (position < 1):
        return y
    else: 
        return get_fib(position -1)+ get_fib(position-2)
        