def calculator():
    print("Calculator")
    print("Operation : + , - , * , / ")
    n=float(input("Enter the first digit:"))
    m=float(input("Enter the second digit:"))
    op=input("Enter an operation - [+,-,*,/]")
    if op=="+":
        r=n+m
    elif op=="-":
        r=n-m
    elif op=="*":
        r=n*m
    elif op=="/":
        if m==0:
            print("Error  Invalid Syntax")
        r=n/m
    else:
        print("Invalid Operation")
        print("Please enter +,-,*,/")
        return
    print(f"Result: {n} {op} {m} = {r}")

calculator()