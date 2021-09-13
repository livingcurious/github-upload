#!/usr/bin/python3

import os
flag_file=open('flag.txt', 'r')
flag =flag_file.read();
def returnFlag():
return flag

print(returnFlag())
    flag_file.close()
# Python script which just returns the flag #
