numbers = [2,3,4,5,6,8,9]
print(type(numbers))
for i in numbers:
    if(i%2==0):
        print(i,"even")
    else:
        print(i,"odd")
#range()
for i in range(1,10,2):
    print(i)
#while
count = 0
while(count<10):
    print("value of i", count)
    count=count+1
print("done")