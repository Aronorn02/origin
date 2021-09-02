max_num = int(input("Input maximum number: "))

for i in range(max_num+1):
    summa = 0

    for j in str(i):
        summa += int(j)

    if (summa**3 == i) and (i != 0):
        print(i)
