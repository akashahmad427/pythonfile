n=5
print('total seats are ',n)
while True:
    name=input('enter your name = ')
    m=int(input('enter number of seats = '))
    if m<=n:
        f=n-m
        print(f'{name} gain {m} seats')
        print('remaining seats are',f)
        n=f
        if n==0:
            print('all seats are fill')
            break
    else:
        print(f'{name} sorry your not elligible for this remaining seats are {n}')
