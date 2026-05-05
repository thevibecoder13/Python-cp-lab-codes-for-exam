
class NegativeNumberError(Exception):
    pass
while True:
    try:
        num = int(input("Enter a positive integer: "))
        
        if num < 0:
            raise NegativeNumberError("Negative numbers are not allowed!")
        
        print("Valid input:", num)
        break

    except NegativeNumberError as e:
        print("Error:", e)
    
    except ValueError:
        print("Error: Invalid input! Please enter an integer.")