# check if a no. is divisible by 3 and last digit is 4.   

num=int(input("Enter number: "))
if (num % 3==0) and (num % 10==4):
    print("The number is divisible by 3 and last digit is 4.")
else:
    print("The number does not divisible by 3.")