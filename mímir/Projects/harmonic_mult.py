option = ""

while option != "q":
    option = input("(h)armonic, (m)ultiplication or (q)uit: ")


    if option == "h":

        n = int(input("Series length: "))
        denominator = 1
        h_sum = 0

        for i in range(n):
            # Stækkar summuna og nefnarann í hverri lykkju.
            print(round(1/denominator, 4))
            h_sum += 1/denominator
            denominator +=1

        print("Sum of series: " + str(round(h_sum, 4)))


    elif option == "m":

        first = int(input("First integer: "))
        second = int(input("Second integer: "))

        m_sum = 0

        while second != 0:
            # Ef seinni talan er oddatala þá bætist hún í summuna.
            if second % 2 == 1:
                m_sum += first
            
            print(str(first) + " " + str(second))

            first *= 2
            second //= 2
        
        print("Product: " + str(m_sum))
    

    elif option == "q":
        # Kemur í veg fyrir að fá "Illegal choice" þegar maður hættir.
        break


    else:
        print("Illegal choice!")

