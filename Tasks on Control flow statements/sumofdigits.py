num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10       # take last digit
    sum_of_digits += digit # add to sum
    num = num // 10        # remove last digit
print("Sum of digits:", sum_of_digits)