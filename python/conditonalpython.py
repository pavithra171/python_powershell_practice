'''state = input("entre sentence:")
text = input("enter another sentence:")
if(len(state)==len(text)):
    print("entered string are equal")'''
a = int(input("enter number: "))
b = int(input("enter another number: "))
select = int(input("1.addition\n, 2.substraction\n, 3.multiplication\n, 4.division\n, 5.modulous\n, 6.exponential\n, 7.floordivision\n"))
if(select==1):
    print(a+b)
elif(select==2):
    print(a-b)
elif(select==3):
    print(a*b)
elif(select==4):
    print(a/b)
elif(select==5):
    print(a%b)
elif(select==6):
    print(a**b)
elif(select==7):
    print(a//b)
else:
    print("none")