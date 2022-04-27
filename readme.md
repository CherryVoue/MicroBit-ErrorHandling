# Simple Error Handling with the Micro:Bit
This simple division calculator lets the user repeatedly attempt calculations.

Non-number input will trigger the `TypeError` or `ValueError` exceptions, which print "Expected a number." Trying to divide a number by zero will trigger the `ZeroDivisionError` exception, and print "Can't divide by zero."

All exceptions will prompt the user to try another calculation.
