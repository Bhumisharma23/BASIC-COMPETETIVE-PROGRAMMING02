# read a number and check if a number is divisible by 7 or last digit is 5.

num=int(input("Enter number: "))
if (num % 7==0) and (num % 10==5):
    print("The number is divisible by 7 and last digit is 5.")
else:
    print("The number does not divisible by 7.")