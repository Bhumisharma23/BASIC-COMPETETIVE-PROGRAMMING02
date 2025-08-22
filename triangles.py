#triangles

agl1=float(input("Enter 1st angle: "))
agl2=float(input("Enter 2nd angle: "))
agl3=float(input("enter 3rd angle: "))
if (agl1+agl2+agl3==180 and agl1>0 and agl2>0 and agl3>0):
    if  (agl1==90 or agl2==90 or agl3==90):
        print("Right angle")
    elif (agl1>90 or agl2>90 or agl3>90):
        print("Obtuse angle")
    else:
        print("Acute angle")
    
