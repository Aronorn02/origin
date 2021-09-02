num_int = int(input("Enter a number: ")) # Do not change this line

# Fill in the missing code below
if num_int <= 0:
    print("The number is too small.")

elif num_int % 2 == 0:
    counter = 2
    while counter <= num_int:
        print(counter)
        counter += 2


elif num_int % 2 == 1:
    counter = 1
    while counter <= num_int:
        print(counter)
        counter += 2