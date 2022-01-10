# Summing numbers
def summer(nums):
    total = 0
    numbers = nums.split(" ")
    for num in numbers:
        total += int(num)
    return total

print(summer(input("Enter nums: ")))


