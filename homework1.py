
#N number of prime numbers

num=int(input("enter the number: "))
x =2
while num!=0:
    for i in range(2,x):
        if x%i==0:
            break
    else:
         print(x,end= " ")
         num -= 1
    x += 1
