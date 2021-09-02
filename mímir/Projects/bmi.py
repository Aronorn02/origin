# Tökum fyrst við tölunum
stones = float(input("Weight in stones: "))
pounds = float(input("Extra pounds: "))
feet = float(input("Height in feet: "))
inches = float(input("Extra inches: "))

# Breitum um mælieiningar og reiknum síðan BMI
kg = stones*6.3503 + pounds*0.4540
cm = feet*30.48 + inches*2.54
BMI = kg/((cm/100)**2)

# Gerum auða línu á milli inntaksins og úttaksins
print("")

# Hér skilum við úttakinu, námundað með einum aukastaf
print("kg: " + str(round(kg, 1)))
print("cm: " + str(round(cm, 1)))
print("BMI: " + str(round(BMI, 1)))
