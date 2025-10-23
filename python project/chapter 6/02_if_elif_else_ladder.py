a = int(input("enter your age : "))
if(a>=18):
    print("you are above the age of consent")
    print("good for you")

elif(a<0):
    print("you are entering a invalid negative age")

elif(a==0):
    print("you are entering 0 which are invalide age")

else:
    print("you are below the age of consent")

print("end of program")