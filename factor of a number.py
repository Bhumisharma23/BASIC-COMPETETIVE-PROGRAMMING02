# print all factors/ divisor of a given +ve number.

num=int(input("Enter a number: "))
i=1
while(i<=num):
    if(num%i==0):
        print(i)
    i+=1