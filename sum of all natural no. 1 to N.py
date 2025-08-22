# sum of all natural numbers 1 to N

N=int(input("Enter a number: "))
total=0
for i in range (1,N+1):
    total=total+i
print("sum= ",total)