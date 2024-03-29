


def fahrenheit(c):
    """Returns the input Celsius degrees in Fahrenheit"""
    return (9/5) * c + 32

def celsius(f):
    """Returns the input Fahrenheit degrees in Celsius"""
    return (5/9) * (f - 32)

"""
Call the functions below the function definitions.
"""

c = float(input('Enter degrees in Celsius:'))
f = fahrenheit(c)

# You can print multiple items in one statement. If you put a comma after each item, it prints a space and then goes
# on the print the next item.
print(c, 'C =', f, 'F')

# You can print this way too, but allowing exactly two decimal places.
print('%.2f C = %.2f F' % (c, f))

f = float(input('Enter degrees in Fahrenheit:'))
c = celsius(f)
print(f, 'F =', c, 'C')
print ('%.2f F = %.2f C' % (f, c))

'''
Try composition of functions
Converting a Fahrenheit temperature to Celsius and Back to Fahrenheit should give you the original
'''

print()
f = float(input('Enter degrees in Fahrenheit:'))

# Use assert to check returned value is equal to the expected value
assert fahrenheit(celsius(f)) == f
# No output should be produced, unless the assertion fails, which means you have an error (either in code
# or your expectation).