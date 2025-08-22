# write a program that takes a positive integer N as input from the user and
#prints all natural no. from 1 to N with each no. followed by a space.

N=int(input("Enter a number: "))
for i in range(1,N+1):
    print(i,end=" ")