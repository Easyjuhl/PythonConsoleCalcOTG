#A simple calculator
while True:
    print(""" 
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
        a = float(in1)
        b = float(in2) 
        c = a+b
        output = "{} + {} = {}".format(a, b, c)
        print(output)
    elif slct == "sub":
        in1 = input("Write a number: ").lower()
        in2 = input("Write another number: ").lower()
        a = float(in1)
        b = float(in2) 
        c = a-b
        output = "{} - {} = {}".format(a, b, c)
        print(output)
    elif slct == "mul":
        in1 = input("Write a number: ").lower()
        in2 = input("Write another number: ").lower()
        a = float(in1)
        b = float(in2) 
        c = a*b
        output = "{} * {} = {}".format(a, b, c)
        print(output)
    elif slct == "div":
        in1 = input("Write a number: ").lower()
        in2 = input("Write another number: ").lower()
        a = float(in1)
        b = float(in2) 
        c = a/b
        output = "{} / {} = {}".format(a, b, c)
        print(output)
    else:
        break
