nums = int(input("How many numbers would you like to generate? "))
numbers = []
num1 = 0
num2 = 1

for x in range(nums):
    if x < 2:
        numbers.append(1)
    else:
        numbers.append(num1 + num2)
        num1, num2 = num2, num1 + num2

numbers.pop(0)
print("Here is your sequence:", numbers)

sum_even = 0
for x in range(len(numbers)):
    if numbers[x] % 2 == 0:
        sum_even += numbers[x]

print("The sum of all even numbers is ", sum_even)
