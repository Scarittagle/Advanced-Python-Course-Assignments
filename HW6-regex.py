#REGEX HOMEWORK
#WEIWEI SU
#U17420699
#Last modification date: 11/5/2017

import re
# if you need any other imports, put them below


class BadPasswordCharacter(Exception):
    pass

class InvalidFractionExpression(Exception):
    pass

def strong_pwd(pwd_string):
    try:
        prog = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{8,}$') #That's atleast 8 char, 1 Upper, 1 Lower, 1 Digit and Only letters and digits
        #Check string
        result = prog.match(pwd_string)
    except BadPasswordCharacter as result: #Since the custom Exception class did not contain anything it shouldn't output the message though.
        print ("The password is not strong enough.")

def clear_whitespace(s):
    prog = re.compile(r"\s+")
    result = prog.sub("", s)
    print(result)

def extract_from_equation(s):
    #clear whitespaces
    input = clear_whitespace(s)

    #Extract
    prog = re.compile(r'(\d+)/(\d+)([+\-*\/])(\d+)/(\d+)')
    #Check Format
    try:
        Expression = prog.match(s)
    except InvalidFractionExpression as Expression: #If the format isn't right (Which will return 'None' by regex.match(), an Exception is raised here.
        print ("The format is not right.")
    finally:
        firstNumerator = Expression.group(1)
        firstDominator = Expression.group(2)
        operator = Expression.group(3)
        secondNumerator = Expression.group(4)
        secondDominator = Expression.group(5)

    #Print
    print ("First Numerator: " + firstNumerator)
    print ("First Dominator: " + firstDominator)
    print ("Operator: " + operator)
    print ("Second Numerator: " + secondNumerator)
    print ("Second Dominator: " + secondDominator)