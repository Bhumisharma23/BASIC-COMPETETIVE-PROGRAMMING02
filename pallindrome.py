 # pallindrome

N=int(input("Enter a number: "))
original=N
rev=0
while N>0:
    digit=N%10
    rev=rev*10+digit
    N=N//10
if original == rev:
    print("Yes")
else:
    print("No")