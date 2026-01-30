''' Developed by 'Asian IT Tech' '''

'''
def Coffee():
    Name = "Espresso Coffee"
    Price = 199
    quentity = 2 
    TotalPrice = quentity * Price

    print(f'Coffee Name: {Name}\nQuentity : {quentity}\nTotalPrice : {TotalPrice}\nThank You Sir.')

Coffee()

while True :
    print(f'---------------\n1. Espresso Coffee\n2. Americano Coffee\n3. Cappuccino Coffee\n4. Latte Coffee\n5. Mocha Coffee\n6. Exit\n---------------')
    userinput = int(input('Order Please :'))

    if userinput == 1:
        Name = "Espresso Coffee"
        Price = 199
        quentity = 2 
        TotalPrice = quentity * Price

        print(f'Coffee Name: {Name}\nQuentity : {quentity}\nTotalPrice : {TotalPrice}\nThank You Sir.')

'''

n =3
if n % 2 ==0:
    print('even')
else:
    print('odd')
