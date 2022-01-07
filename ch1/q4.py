# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n
def square(n):
    n = int(n)
    if n > 0:
        return n * n + square(n - 1)
    return 0

print(square(input("Enter positive number: ")))

