a = int(input("enter your age : "))

if(a%2==0):
    print(a ,"is even")

if(a>=18):
    print("you are above the age of consent")
    print("good for you")

elif(a<0):
    print("you are entering a invalid negative age")

else:
    print("you are below the age of consent")

print("end of program")


