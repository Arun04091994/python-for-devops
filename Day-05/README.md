**we can pass commandline arguments using **sys** module**

**example**

import sys
def add(num1, num2):
    addition = num1 + num2
    return addition

##to store command line arguments to variables##
num1 = float(sys.argv[1]) --> with out float it will take it as a string and concatinates both strings
operation = sys.argv[2]
num2 = float(sys.argv[3])

##calling function by checking the operation condition##
if operation == "add"
    print(add(num1, num2))

command line argument should be like below
python filename.py 2 add 3

How to export sensitive information and retrieve value
**os**: **module we use to store sensitive information**

**example**

import os

##to read environment variables in python file##
print(os.getenv("apitoken"))

##to export api token with command line argument###
export apitoken="jgjjjhkkjkj"

**commands for listing environment variables, modules installed**

env
pip list

