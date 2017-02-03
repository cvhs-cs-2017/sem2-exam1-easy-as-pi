"""Write a program that will take a Binary number and return its Whole Number Value:

example:  10011 would return (16+0+0+2+1 = 19)"""

def BinaryToNum(num):
    length = len(num)
    tracker = 0
    ind = 0
    for i in num:
        new = (int(num[ind])*(2**(length-(ind+1))))
        tracker += new
        ind += 1
    return tracker
print(BinaryToNum("10011"))

"""Write a program that would take a real number value and convert it into BINARY"""
"""
def NumToBinary(num2):
    import math
    binary = ''
    while num2 != 0:
        Floorlog2 = math.floor(math.log(int(num2),2))

    return floor
print(NumToBinary('9'))
"""

def NumToBinary(num2):
    import math
    Floorlog = math.floor(math.log(int(num2),2))
    binary = ''
    while num2 != 0:
        binarynum = math.floor((num2/(2**Floorlog)))
        binary += str(binarynum)
        if binarynum != 0:
            num2 = num2 - (2**Floorlog)
        Floorlog -= 1
    return binary
    #return binarynum
print(NumToBinary(9))
