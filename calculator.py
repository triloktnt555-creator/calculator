def add(a , b):
    return a+b

def subtract(a , b):
    return  a-b

def multiply(a , b):
    return  a*b

def divide(a , b):
    return  a/b

print("---command for calculation---")
print("Click 1 for add(+)")
print("Click 2 for subtract(-)")
print("Click 3 for multiply(*)")
print("Click 4 for divide(/)")
print("Click 5 for exit.....")

while True:
    choice=int(input("Enter your choice: "))
    

    match choice:
        case 1:
            num1=float(input("Enter number1: "))
            num2=float(input("Enter number2: " ))
            print("Result: " ,round(add(num1,num2),2))
        case 2:
            num1=float(input("Enter number1: "))
            num2=float(input("Enter number2: " ))
            print("Result: " ,round(subtract(num1,num2),2))
        case 3:
            num1=float(input("Enter number1: "))
            num2=float(input("Enter number2: " ))
            print("Result: " ,round(multiply(num1,num2),2))
        case 4:
            num1=float(input("Enter number1: "))
            num2=float(input("Enter number2: " ))
            try:
                print("Result: " ,round(divide(num1,num2),2))
            except :
                print("division by zero is not possible")
        case 5:
            print("Exiting...")
            break ;

        case _:
            print("Invalid! Enter choice from 1 to 5")
        
    