size = int(input("How large is the square?: "))

# Write your solution here below


print("* "*(size-1) + "*")
if size > 1:
    for i in range(size-2):
        print("*" + " "*((size*2)-3) + "*")

    print("* "*(size-1) + "*")