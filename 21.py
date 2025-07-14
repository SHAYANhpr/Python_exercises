def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: taghsim bar sefr emkan pazir nist.")
        return None

while True:
    try:
        num1 = int(input("Enter the number 1: "))
        num2 = int(input("Enter the number 2: "))
        result = divide(num1, num2)
        if result is not None:
            print("Result:", result)
            break
    except ValueError:
        print("Error: faghat adad vared konid.")
    finally:
        print("barname ba movafaghiat egra shod!\n")