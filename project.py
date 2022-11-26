import random

#Requirment for Password
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*//"


use_for = lower_case + upper_case + number + symbols
length = int(input("Length: "))
password = "".join(random.sample(use_for,length))

if length < 12 :
    print("Required length is 12 or more than 12")
else:
    print(password)
