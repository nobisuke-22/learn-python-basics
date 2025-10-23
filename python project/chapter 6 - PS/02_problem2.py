a1 = int(input(" enter marks in subject 1 : "))
a2 = int(input(" enter marks in subject 2 : "))
a3 = int(input(" enter marks in subject 3 : "))

if( ((a1+a2+a3)/3)*100 >=40 and a1>33 and a2>33 and a3>33):
    print(" student is passed ")
else:
    print(" student is failed")