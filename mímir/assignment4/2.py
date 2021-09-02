n = int(input("Enter how many numbers you want to input(>0): ")) # Do not change this line

# Fill in the missing code
oldhighnum = 0
oldlownum = 9**999


for i in range(n):
    number = int(input("Enter an integer: "))
    if number > oldhighnum:
        max_num = number
        oldhighnum = number
    if number < oldlownum:
        min_num = number
        oldlownum = number
    




print("Highest number from input:", max_num)
print("Lowest number from input:", min_num)