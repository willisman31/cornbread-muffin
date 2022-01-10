def is_multiple(n, m):
    return int(n) % int(m) == 0

n = input("Choose first number: ")
m = input("Choose second number: ")
print(is_multiple(n, m))

