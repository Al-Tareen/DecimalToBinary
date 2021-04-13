#Decimal to binary converter 

#using fmod for remainder purposes
from math import fmod as remain

#user input
number = int(input("Please enter your decimal value.\n"))

#initial quotient
quotient = number

#emptyt binary list
binary = []

#declared remainder var
remainder = int

while quotient != 0:
    if remain(quotient, 2) == 1:
        binary.insert(0, 1)
        quotient = (quotient-1)/2
        continue
    else:
        binary.insert(0, 0)
        quotient = quotient/2
        continue

#Returns the concatenation of all elements in the passed list
def ListToString(list):
    decimal = ''
    for element in list:
        decimal += str(element)
    return decimal 

print("Your decimal,", number, "in binary is", ListToString(binary) + ".")