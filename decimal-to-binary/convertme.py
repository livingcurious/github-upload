#!/usr/bin/python3
import sys
if len(sys.argv)==2:
    def decimalToBinary(n):  
        return bin(n).replace("0b", "")

else:
    print("Please input the number to get Binary equivalent")
    exit()
# decimal number
number = int(sys.argv[1])
print(decimalToBinary(number))