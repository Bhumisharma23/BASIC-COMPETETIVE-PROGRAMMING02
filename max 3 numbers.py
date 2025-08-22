#WAP to input three numbers (A, B & C) from the user and print the minimum element among A, B & C.

A=int(input("Enter a number: "))
B=int(input("Enter a number: "))
C=int(input("Enter a number: "))
if (A<B) and (A<C):
    print("A is minimum")
elif (B<A) and (B<C):
    print("B is minimum")
else:
    print("C is minimum")