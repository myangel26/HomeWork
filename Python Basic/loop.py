number = 0

while number % 2 == 0:
    number = int(input('Input a number : '))
    if number % 2 == 0:
        print("Sorry, the number you enter is even number!")
    else:
        for i in reversed(range(1, number + 1)):
            if i % 2 != 0:
                a = ''.join(map(str, [i]*i))
                print(a.center(number))

print("------------------------------------------------------")

array = []
array2 = []
array3 = []
for i in range(1, 101):
    array.append(i)

for k in array:
    if k % 3 == 0:
        array2.append(k)
print(array2)

for k in array:
    if k % 5 == 0:
        array3.append(k)
print(array3)