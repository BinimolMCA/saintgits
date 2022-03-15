a=int(input("Enter the no : "))
b=int(input("Enter the no : "))
r=1

if a<b :
    a,b=b,a
    
if a==0:
    print("gcd(",a,",",b,") = ",b)
elif b==0:
    print("gcd(",a,",",b,") = ",a)
else :
    while(r!=0) :
        r=a%b
        a,b=b,r
        print("gcd(",a,",",b,") = ",a)
