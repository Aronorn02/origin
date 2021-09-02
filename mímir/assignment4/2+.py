# Don't change the following lines
import math

number_of_cycles = float(input("Number of cycles: "))
number_of_lines = int(input("Stretched over how many lines? "))

radians_per_line = number_of_cycles * 2 * math.pi / number_of_lines

# ...now fill in the rest
for line_number in range(number_of_lines):
    change = round(20 * (1 + math.sin(line_number*radians_per_line)))
    print("X"*change)

