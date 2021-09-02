# Upphafsstillum breytur
money = 0
sales = 0
running = True

print("Welcome to Dunder Mifflin!")

while running == True:
    another_sale = input("Would you like to add a sale (y/n)?: ")

    if another_sale == "y":
        paper_or_printer = input("paper or printer: ")

        if paper_or_printer == "paper":
            paper_num = int(input("# of paper piles: "))

            # pappírsbúnkinn kostar 10$ og launin eru 15% fyrir hvern búnka
            money += paper_num * 10 * 0.15
            sales += 1

            print("You've made " + str(int(money)) + " today with " + str(int(sales)) + " sales")

        elif paper_or_printer == "printer":
            printer_num = int(input("# of printers: "))

            # hver prentari kostar 150$ og launin eru 30% fyrir hvern prentara
            money += printer_num * 150 * 0.3
            sales += 1

            print("You've made " + str(int(money)) + " today with " + str(int(sales)) + " sales")
        
        else: 
            print("You did neither type in paper nor printer")
            print("You've made " + str(int(money)) + " today with " + str(int(sales)) + " sales")
    
    if another_sale == "n":
        # Ef kaupandi vill ekki kaupa meira þá er hætt að spyrja hann
        running = False