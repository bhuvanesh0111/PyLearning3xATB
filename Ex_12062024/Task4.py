num=int(input('Enter the range: '))
n1=0
n2=1
for i in range(0,num):
    if (i<=1):
        fib=i
    else:
        fib=n1+n2
        n1=n2
        n2=fib
        print(fib)