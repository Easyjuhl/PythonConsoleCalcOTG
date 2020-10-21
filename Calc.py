#A simple calculator
from time import sleep
from sympy import symbols, Eq, solve, diff
x, y, a, b, c, d = symbols('x y a b c d')
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
    Smt: Smoother

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
    elif slct == "smt":
        print("Write functions:")
        f1 = eval(input("f1: ").replace("^", "**"))
        f2 = eval(input("f2: ").replace("^", "**"))
        print("Vælg interval")
        in1 = input("Write a number: ")
        in2 = input("Write another number: ")
        try:
            inn1 = float(in1)
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in1))
            sleep(3)
            break
        try:
            inn2 = float(in2)
        except ValueError:
            print("Error: Your input {} is not a valid input".format(in1))
            sleep(3)
            break
        eq1 = Eq(a*inn1**3 + b*inn1**2 + c*inn1 + d, f1.subs(x, inn1))
        eq2 = Eq(a*inn2**3 + b*inn2**2 + c*inn2 + d, f2.subs(x, inn2))
        eq3 = Eq(3*a*inn1**2 + 2*b*inn1 + c, diff(f1, x).subs(x, inn1))
        eq4 = Eq(3*a*inn2**2 + 2*b*inn2 + c, diff(f2, x).subs(x, inn2))
        sol = solve((eq1, eq2, eq3, eq4), (a, b, c, d))
        print("{}*x^3 + {}*x^2 + {}*x + {}".format(sol[a], sol[b], sol[c], sol[d]))
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
