# Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise.  However, your function cannot use modulo, multiplication, or division operators
def is_even(k):
    temp = str(k)[-1]
    return temp == '0' or temp == '2' or temp == '4' or temp == '6' or temp == '8'

k = input("Enter number: ")
print(is_even(k))

