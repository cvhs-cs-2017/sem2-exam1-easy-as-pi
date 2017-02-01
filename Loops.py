"""Write a program that will add 5 and loop until it reaches a number GREATER
than 100.  It should then spit out the result AND tell the user how many times
it had to add 5 (if any)"""

print('Enter a number.')
num = int(input())
counter = 0
num2 = num
while num2 <= 100:
    num2 += 5
    counter += 1
print('If you keep on adding 5 to', str(num) + ", the first number above 100 is", str(num2), 'and it will take', str(counter), 'steps to reach there.')

"""Write a program that will prompt the user for an input value (n) and double
it IF is an ODD number, triple it if is an EVEN number and do nothing if it is
anything else (like a decimal or a string)"""
