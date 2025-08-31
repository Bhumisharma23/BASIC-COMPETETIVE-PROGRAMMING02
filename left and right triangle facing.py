# 9. Left and right triangles facing each other
n = int(input("enter a number: "))
for i in range(n, 0, -1):
    print("*" * i, end=" ")
    print(" " * (2*(n-i)), end=" ")
    print("*" * i)

print()
