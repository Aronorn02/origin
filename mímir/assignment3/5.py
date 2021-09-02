k = int(input("Enter value for k: ")) # Do not change this line

# Fill in the missingcode below

summa = 0

while summa <= k:
    num = int(input("Enter a value: "))
    summa += num
if summa > k:
    summa -= num

print("Sum: " + str(summa))

