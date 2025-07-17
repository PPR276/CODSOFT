import random
a = [['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/',
    '`', '~'],['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'],['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'],['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
b = int(input("Enter the Length of password of your choice \n(the length should be 4 or greater than 4 for better complexity): "))
c=""
if b>=4:
    if b == 4:
        d=random.choice(a[0])
        c=c+d
        d=random.choice(a[1])
        c=c+d
        d=random.choice(a[2])
        c=c+d
        d=random.choice(a[3])
        c=c+d
        print(c)
    if b > 4:
        d=random.choice(a[0])
        c=c+d
        d=random.choice(a[1])
        c=c+d
        d=random.choice(a[2])
        c=c+d
        d=random.choice(a[3])
        c=c+d
        for i in range(b-4):
            e=random.choice(a)
            f=random.choice(e)
            c=c+f
        print(f"Your password is : {c}")