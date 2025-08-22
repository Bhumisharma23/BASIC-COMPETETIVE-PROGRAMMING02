# WAP to input two numbers (A & B) from the user and print the maximum element among A&B.

A=int(input("Enter a number: "))
B=int(input("Enter a number: "))
if (A>B):
    print("A is max")
elif(B>A):
    print("B is max")
else:
    print("Both numbers are equal")