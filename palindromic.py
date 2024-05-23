num = int(input("Enter a number: "))
temp = num

if (num <= 0):
    print("Please enter just positive numbers!")

else:
    newNum = 0
    j = 10 ** (len(str(num)) - 1)

    while num > 0:
        digit = num % 10
        newNum += digit * j
        num //= 10
        j /= 10

    newnum = int(newNum)

    if (newnum == temp):
        print(f"{temp} is a Palindromic!")

    else:
        print(f"{temp} isn't a Palindromic!")
