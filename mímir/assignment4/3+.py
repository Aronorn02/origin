
# Read exactly four lines of input
line1 = input()
line2 = input()
line3 = input()
line4 = input()


# Define variables for the range of numbers within which we have 'printable' characters.
# As we shift the input characters, we must ensure that they stay within this range.
LOW = ord(" ")  # 32
HIGH = ord("~") # 126

# Every transmission starts with the line "Hail Caesar!" so the first letter, 
# once decrypted, must be H.
first_letter = line1[0]
# ...now find out what the key is
key = ord(first_letter) - ord("H")
# We can use 'for' to iterate over the lines and decrypt them one by one

for line in (line1, line2, line3, line4):
    newline = ""
    for letter in line:
        ascii = ord(letter)
        if (ascii == HIGH) and key < 0:
            ascii = LOW
        else:
            ascii -= key
        newline = newline + str(chr(ascii))
    print(newline)