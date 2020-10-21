#A simple calculator
from time import sleep
while True:
    print(""" 
     _____       _            _       _             
    /  __ \     | |          | |     | |            
    | /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
    | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
     \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                
    Add: Addition
    Sub: Substraction
    Mul: Multiplication
    Div: Division
    Ave: Average

    Write quit to quit

    """)
    slct = input("Select: ").lower()
    if slct == "add":
        in1 = input("Write a number: ").lower()
        in2 = input("Write another number: ").lower()
        try:
            a = float(in1)
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in1))
            sleep(3)
            break
        try:
            b = float(in2) 
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in2))
            sleep(3)
            break
        c = a+b
        output = "{} + {} = {}".format(a, b, c)
        print(output)
    elif slct == "sub":
        in1 = input("Write a number: ").lower()
        in2 = input("Write another number: ").lower()
        try:
            a = float(in1)
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in1))
            sleep(3)
            break
        try:
            b = float(in2) 
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in2))
            sleep(3)
            break
        c = a-b
        output = "{} - {} = {}".format(a, b, c)
        print(output)
    elif slct == "avg":
        lst = []
        amountstr = input("Amount of operands: ")
        try:
            amountint = int(amountstr) 
        except ValueError:
            print("Error: Your input {} is not a valid input".format(amountstr))
            sleep(3)
            break
        for inn in range(amountint):
            ite = inn + 1
            in1 = input("Number " + str(ite) + ": ")
            try:
                a = float(in1) 
            except ValueError:
                print("Error: Your input {} is not a valid input".format(in1))
                sleep(3)
                break
            lst.append(a)
        b = sum(lst)
        c = b/amountint
        output = "{} / {} = {}".format(b, amountint, c)
        print(output)            
    elif slct == "mul":
        in1 = input("Write a number: ").lower()
        in2 = input("Write another number: ").lower()
        try:
            a = float(in1)
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in1))
            sleep(3)
            break
        try:
            b = float(in2) 
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in2))
            sleep(3)
            break
        c = a*b
        output = "{} * {} = {}".format(a, b, c)
        print(output)
    elif slct == "div":
        in1 = input("Write a number: ").lower()
        in2 = input("Write another number: ").lower()
        try:
            a = float(in1)
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in1))
            sleep(3)
            break
        try:
            b = float(in2) 
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in2))
            sleep(3)
            break
        c = a/b
        output = "{} / {} = {}".format(a, b, c)
        print(output)
    elif slct == "quit":
        break
    else:
        print("Error: Your input {} is not a valid input".format(slct))
        sleep(3)
        break
