#Read N, print sum of digits in N

num=int(input("Enter number: "))
sum=0
while(num>0):
    digit=num%10
    num=num//10
    sum+=digit
print(sum)