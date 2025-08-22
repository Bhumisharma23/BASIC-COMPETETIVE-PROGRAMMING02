agl1=int(input("Enter first angle: "))
agl2=int(input("Enter second angle: "))
agl3=int(input("Enter third angle: "))
if agl1>0 and agl2>0 and agl3>0 and (agl1+agl2+agl3==180):
    print("Triangle is valid")
else:
    print("Triangle is not valid")