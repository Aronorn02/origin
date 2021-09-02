n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
k = 2
prime = True
if n ==1:
    prime = False
while k < n:
    if (n%k == 0):
        prime = False
        break
    else:
        prime = True
        k +=1


# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")
