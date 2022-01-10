# Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two.  Do not use built-in functions min or max in implementing your solution
def minmax(data):
    data.sort()
    return (data[0], data[-1])

def in_list():
    data = []
    while True:
        try:
            data.append(int(input("Enter your next number: ")))
        except ValueError:
            break
    return data

print(minmax(in_list()))

