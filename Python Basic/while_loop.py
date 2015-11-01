__author__ = 'ADMIN'

import random
from random import randint
# print(randint(0,9))
# print(random.randrange(0, 101, 3))
"""
number_select = random.randint(0,101)

while True:
    number = int(input('Nhap vao 1 so:'))
    if number == number_select:
        print('Cool,correct')
        break
    elif number < number_select:
        print("Your number is less than your number computer")
    elif number > number_select:
        print("Your number is heigher than your number computer")
"""

###########################################
# HomeWork
# tim so chia lon nhat cua 2 so
"""
num1 = int(input('Nhap vao so nguyen thu nhat:'))
num2 = int(input('Nhap vao so nguyen thu hai:'))
gcd = 1
k = 2
while (k <= num1 and k <= num2):
    if ( num1%k == 0 and num2%k == 0):
        gcd = k
    k += 1
print('So chia lon nhat cua %d va %d la: %d' % (num1,num2,gcd))
"""

###########################################
array1 = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin", "muo\i", "tram", "ngan", "trieu", "ty"]
array2 = ["mo^/t", "lam", "le", "muoi"]
num = 125925
# count = len(str(num))

i = 1
s = 0
o = 0
n = 0
tram_ngan = 0
for number in str(num):
    if int(num) // 10 == 0:
        print(array1[num])
    if int(num) // 10 == 1:
        if int(num) == 10:
            print(array1[num])
            break
        if int(number) == 1 and i == 1:
            print(array1[10], end='')
            i = 2
        elif i == 2:
            if int(number) == 5:
                print('', array2[1])
            else:
                print('', array1[int(number)])
    if 2 <= int(num) // 10 <= 9:
        if int(num) % 2 == 0:
            print(array1[int(number)], array2[3])
            break
        if i == 1:
            print(array1[int(number)], array2[3], end='')
            i = 2
        else:
            if int(number) == 5:
                print('', array2[1])
            elif int(number) == 1:
                print('', array2[0])
            else:
                print('', array1[int(number)])
    if 1 <= int(num) // 100 <= 9:
        if int(num) % 100 == 0:
            print(array1[int(number)], array1[11])
            break
        if i == 1:
            print(array1[int(number)], array1[11], end='')
            i = 2
        elif i == 2:
            if int(number) == 0:
                print('', array2[2], end='')
                i = 3
            elif int(number) == 1:
                print('', array1[10], end='')
                i = 3
                s = 1
            else:
                print('', array1[int(number)], array2[3], end='')
                i = 3
                s = 1
                o = 1
        elif i == 3:
            if int(number) == 0:
                break
            elif int(number) == 1:
                if o == 1:
                    print('', array2[0])
                else:
                    print('', array1[int(number)])
            elif int(number) == 5:
                if s == 1:
                    print('', array2[1])
                elif s == 0:
                    print('', array1[int(number)])
            else:
                print('', array1[int(number)])
    if 1 <= int(num) // 1000 <= 9:
        if int(num) % 1000 == 0:
            print(array1[int(number)], array1[12])
            break
        if i == 1:
            print(array1[int(number)], array1[12], end='')
            i = 2
        elif i == 2:
            print('', array1[int(number)], array1[11], end='')
            i = 3
        elif i == 3:
            if int(number) == 0:
                print('', array2[2], end='')
                i = 4
            elif int(number) == 1:
                print('', array1[10], end='')
                s = 1
                i = 4
            else:
                print('', array1[int(number)], array2[3], end='')
                i = 4
                s = 1
                o = 1
        elif i == 4:
            if int(number) == 0:
                break
            elif int(number) == 1:
                if o == 1:
                    print('', array2[0])
                else:
                    print('', array1[int(number)])
            elif int(number) == 5:
                if s == 1:
                    print('', array2[1])
                elif s == 0:
                    print('', array1[int(number)])
            else:
                print('', array1[int(number)])
    if 1 <= int(num) // 10000 <= 9:
        if int(num) % 10000 == 0:
            if int(num) / 10000 == 1:
                print(array1[10], array1[12])
                break
            else:
                print(array1[int(number)], array2[3], array1[12])
                break
        if i == 1:
            if int(number) == 1:
                print(array1[10], end='')
                i = 2
                n = 1
            else:
                print(array1[int(number)], end='')
                i = 2
        elif i == 2:
            if n == 1:
                if int(number) == 0:
                    print('', array1[12], end='')
                    i = 3
                elif int(number) == 5:
                    print('', array2[1], array1[12], end='')
                    i = 3
                else:
                    print('', array1[int(number)], array1[12], end='')
                    i = 3
            else:
                if int(number) == 0:
                    print('', array2[3], array1[12], end='')
                    i = 3
                elif int(number) == 5:
                    print('', array2[3], array2[1], array1[12], end='')
                    i = 3
                else:
                    print('', array2[3], array1[int(int(number))], array1[12], end='')
                    i = 3
        elif i == 3:
            print('', array1[int(number)], array1[11], end='')
            i = 4
        elif i == 4:
            if int(number) == 0:
                print('', array2[2], end='')
                i = 5
            elif int(number) == 1:
                print('', array1[10], end='')
                s = 1
                i = 5
            else:
                print('', array1[int(number)], array2[3], end='')
                i = 5
                s = 1
                o = 1
        elif i == 5:
            if int(number) == 0:
                break
            elif int(number) == 1:
                if o == 1:
                    print('', array2[0])
                else:
                    print('', array1[int(number)])
            elif int(number) == 5:
                if s == 1:
                    print('', array2[1])
                elif s == 0:
                    print('', array1[int(number)])
            else:
                print('', array1[int(number)])
    if 1 <= int(num) // 100000 <= 9:
        if int(num) % 100000 == 0:
            print(array1[int(number)], array1[11], array1[12], end='')
            break
        if i == 1:
            print(array1[int(number)], array1[11], end='')
            i = 2
        elif i == 2:
            if int(number) == 0:
                i = 3
                continue
            elif int(number) == 1:
                print('', array1[10], end='')
                i = 3
                s = 1
            else:
                print('', array1[int(number)], array2[3], end='')
                i = 3
                s = 1
        elif i == 3:
            if 101 <= int(num) // 1000 <= 109:
                print('', array2[2], array1[int(number)], array1[12], end='')
                i = 4
            elif int(num) // 1000 == 100:
                print('', array1[12], array1[12], end='')
                i = 4
            elif int(number) == 5:
                print('', array2[1], array1[12], end='')
                i = 4
            else:
                print('', array1[int(number)], array1[12], end='')
                i = 4
        elif i == 4:
            print('', array1[int(number)], array1[11], end='')
            i = 5
        elif i == 5:
            if int(number) == 0:
                print('', array2[2], end='')
                i = 6
            elif int(number) == 1:
                print('', array1[10], end='')
                i = 6
                s = 1
            else:
                print('', array1[int(number)], array2[3], end='')
                i = 6
        elif i == 6:
            if int(number) == 0:
                break
            elif int(number) == 5:
                if s == 1:
                    print('', array2[1])
                else:
                    print('', array1[5])
            elif int(number) == 1:
                if s == 1:
                    print('', array2[0])
                else:
                    print('', array1[int(number)])
            else:
                print('', array1[int(number)])






