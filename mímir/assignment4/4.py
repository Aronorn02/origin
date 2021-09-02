initial_amount = float(input("Enter the initial amount: ")) # Do not change this line
interest = float(input("Enter the interest(%): ")) # Do not change this line
years = int(input("Enter for how many years: ")) # Do not change this line

current_amount = initial_amount

for i in range(years):
    gain = current_amount*(interest*0.01)
    current_amount += gain


print(f"Amount after {years} years: {round(current_amount, 2)}")