while True:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print("1.Addition\n2.Substraction\n3.Multiplication\n5.Division\n6.Floor division\n7.Modulus\n8.Power")
    ch=int(input("Enter operation: "))
    if ch==1:
        print(a+b)
    elif ch==2:
        print(a-b)
    elif ch==3:
        print(a*b)
    elif ch==4:
        print(a/b)
    elif ch==5:
        print(a//b)
    elif ch==6:
        print(a%b)
    elif ch==7:
        print(a**b)
    else:
        print("Invalid choice")
        break