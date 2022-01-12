# Calculate average from indeterminate number of inputs
def average():
    num = 0
    count = 0
    while True:
        try:
            temp = input("Enter a value: ")
            num += int(temp)
            count += 1
        except ValueError:
            if temp == '': break
            print("Enter a valid number")
    return "Average over " + str(count) + " is " + str(num / count)

print(average())

