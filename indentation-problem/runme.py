#!/usr/bin/python3

import os
flag_file=open('flag.txt', 'r')
flag =flag_file.read();

#print(flag)
def returnFlag():
    return flag

returnFlag()
print(returnFlag())
flag_file.close()
# Python script which just returns the static flag #
