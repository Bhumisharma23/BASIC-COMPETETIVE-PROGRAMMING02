'''for i in range(1,10,2):
    print(i)'''

'''for i in range(1,10,2):
    print(i*i,end=" ")'''

'''n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(i)'''

'''n=int(input("Enter a number: "))
for i in range(1,n+1,2):
    print(i)'''

n=int(input("Enter a number: "))
p=int(input("Enter power: "))
mul = 1
for i in range(p):
    mul=mul*n
    print(mul,end=" ")