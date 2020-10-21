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
            sleep(5)
            break
        try:
            b = float(in2) 
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in2))
            sleep(5)
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
            sleep(5)
            break
        try:
            b = float(in2) 
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in2))
            sleep(5)
            break
        c = a-b
        output = "{} - {} = {}".format(a, b, c)
        print(output)
    elif slct == "mul":
        in1 = input("Write a number: ").lower()
        in2 = input("Write another number: ").lower()
        try:
            a = float(in1)
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in1))
            sleep(5)
            break
        try:
            b = float(in2) 
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in2))
            sleep(5)
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
            sleep(5)
            break
        try:
            b = float(in2) 
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in2))
            sleep(5)
            break
        c = a/b
        output = "{} / {} = {}".format(a, b, c)
        print(output)
    else:
        print("Error: Your input {} is not a valid input".format(slct))
        sleep(5)
        break
