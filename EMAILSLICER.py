print("----------------------------------------------------------------------EMAIL SLICER-----------------------------------------------------------------")
print("-----------------------------------------THIS IS A PROGRAM WHERE YOU CAN SEPERATE A EMAIL INTO USERNAME AND DOMAIN NAME----------------------------")
print()
print()

import re

n = 0
while n < 3:
    s = input("Enter your Email: ")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, s):
        print("Valid Email")
        break
    else:
        print("Invalid Email")
        n += 1

if n == 3:
    print("3 invalid attempts, please try again later")
else:
    a = 0
    h = 0

    while a != 3 and h < 1:
        print()
        print("_________________________________________________________________________MAIN MENU_________________________________________________________________")
        print(">Enter 1 to Print Username")
        print(">Enter 2 to Print Domain name")
        print(">Enter 3 to Print Both")
        print(">Enter 0 to Exit")
        print()
        h += 1
        while True:
            b = s.find('@')
            a = input("Enter Your Input: ")
            c = s[b + 1:len(s) + 1].upper()
            if a == "1":
                print("User Name: " + s[:b])
            elif a == "2":
                print("Domain Name: " + c)
            elif a == "3":
                print("User Name: " + s[:b], " Domain Name: " + c)
            elif a == "0":
                print("~~~~~~~~~~EXITED PROGRAM~~~~~~~~~~")
                break
            else:
                print("Input error")

    print()
    print()
    print("--------------------------------------------------------SUBMITTED BY SANAT KUAMR BHOWIK TO DR. VIPIN KUMAR-----------------------------------------")
    print("----------------------------------------------------------------------------THANK YOU--------------------------------------------------------------")
