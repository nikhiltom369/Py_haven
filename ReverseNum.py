num = int(input("Enter a number: "))
reversed_num = 0
while num != 0:
    rem = num % 10
    reversed_num = reversed_num * 10 + rem
    num //= 10
print("Reversed number:", reversed_num)
