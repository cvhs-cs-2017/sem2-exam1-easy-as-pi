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

print('')
print('Enter an integer')
num = input()
if float(num) % 2 != 0 and float(num) % 2 != 1:
    print('I asked for an integer, not a decimal')
elif int(num) % 2 == 0:
    num3 = int(num)*3
    print(str(num), 'is even. When multiplied by three, answer is', num3)
elif int(num) % 2 == 1:
    num3 = int(num)*2
    print(str(num), 'is odd. When doubled, annwer is', num3)
