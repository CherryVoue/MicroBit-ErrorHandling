# errorHandling.py
from microbit import *

sleep(1000)

print("Division Calculations")

while True:
    try:
        text = input("Enter numerator n: ")
        n = float(text)
    
        text = input("Enter denominator d: ")
        d = float(text)

        q = n / d

    except (TypeError, ValueError):                  
        print("Expected a number.")

    except ZeroDivisionError:
        print("Can't divide by zero.")

    else:
        print("Quotient q: ")
        print("q = n / d")
        print("  = ", n, " / ", d)
        print("  = ", q)

    finally:
        print("Try again!")
        print()
