# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n
def square(n):
    n = int(n)
    if n < 3: # Inclusive
        return 1
    elif n % 2 == 1:
        return n * n + square(n - 2)
    return square(n - 1)

print(square(input("Enter positive number: ")))

