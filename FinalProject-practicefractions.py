#Practice Fractions Project
#Weiwei Su
#U17420699
#Last Modification Date: 11/22/2017

from easygui import *
from fractions import Fraction
import operator
import random
import re
import sys

#Something borrowed from last assignment
def clear_whitespace(s):
    prog = re.compile(r"\s+")
    result = prog.sub("", s)
    return result

#redefine a new isdigit() function to make it accepts negative numbers
def isdigit(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

#Start of the application
while 1:
    #Option interface
    MainWinmsg = "This is a Practicefractions Application for Advanced Python Final Project \n Made by WEIWEI SU \n 11/22/2017 \n\n\n Choose 3 options below to begin."
    MainWintitle = "Practice Fractions"
    MainWinchoice = ["Solve", "Quiz", "Quit"]

    Choice = buttonbox(MainWinmsg, MainWintitle, MainWinchoice, cancel_choice=MainWinchoice[2])

    #Solve Window
    #When Choose Solve
    while Choice == MainWinchoice[0]:
        #Interface
        SolveWinmsg = "Enter an arbitrary fraction."
        SolveWintitle = "Solve"
        SolvefieldName = ["Equation"]
        SolvefieldValues = []

        SolvefieldValues = multenterbox(SolveWinmsg,SolveWintitle,SolvefieldName)

        #Check button
        if SolvefieldValues:
            pass
        else:
            break
        #Check if the entry field is empty
        while 1:
            if SolvefieldValues == None:
                break
            errmsg = ""
            for i in range(len(SolvefieldName)):
                if SolvefieldValues[i].strip() == "":
                    errmsg += ('"%s" is a required field.\n\n' % SolvefieldName[i])
            if errmsg == "":
                break  # no problems found
            SolvefieldValues = multenterbox(errmsg, SolveWintitle, SolvefieldName, SolvefieldValues)

        #Check if the format is correct, if so, solve it.
        while 1:
            #remove white space
            input = clear_whitespace(SolvefieldValues[0])

            #Check format
            Expression = re.compile(r'(\d+)/(\d+)([+\-*\/])(\d+)/(\d+)').match(input)
            if Expression == None:
                msgbox("Format Does not match.", title="EXPRESSION ERROR")
                break
            else:
                # Solve #Code from last assignment
                firstNumerator = Expression.group(1)
                firstDominator = Expression.group(2)
                operators = Expression.group(3)
                secondNumerator = Expression.group(4)
                secondDominator = Expression.group(5)

                if operators == '+':
                    answer = operator.add(Fraction(int(firstNumerator), int(firstDominator)), Fraction(int(secondNumerator), int(secondDominator)))
                if operators == '-':
                    answer = operator.sub(Fraction(int(firstNumerator), int(firstDominator)), Fraction(int(secondNumerator), int(secondDominator)))
                if operators == '*':
                    answer = operator.mul(Fraction(int(firstNumerator), int(firstDominator)), Fraction(int(secondNumerator), int(secondDominator)))

                # Display Answer
                msgbox(answer, title="Solved!")
                break

    #When Choose Quiz
    while Choice == MainWinchoice[1]:
        # Option interface
        QuizWinmsg = "Please choose one of the options below, then it will generate a problem consist with the option you choose with random fractions for you to solve."
        QuizWintitle = "Practice Fractions"
        QuizWinchoice = ["+", "-", "*", "Return"]

        QuizChoice = buttonbox(QuizWinmsg, QuizWinmsg, QuizWinchoice)

        #if picked ' + '
        if QuizChoice == QuizWinchoice[0]:
            #Set Interface value
            #generate Random number
            fx = random.randint(-15, 15)
            fy = random.randint(-15, 15)
            while fy == 0: #in case the denominator gets 0
                fy = random.randint(-15, 15)
            sx = random.randint(-15, 15)
            sy = random.randint(-15, 15)
            while sy == 0: #in case the denominator gets 0
                sy = random.randint(-15, 15)

            QuizWinmsg = "Solve the fractions below: \n (I suggest put fractions down in the answer if you can, except integers)"
            QuizWintitle = "Solve fraction"
            QuizfieldName = [str(fx) + "/" + str(fy) + " + " + str(sx) + "/" + str(sy) + " = "]

            QuizfieldValues = multenterbox(QuizWinmsg, QuizWintitle, QuizfieldName)

            #Check button
            if QuizfieldValues:
                pass
            else:
                break
            # Check if the entry field is empty
            while 1:
                if QuizfieldValues == None:
                    break
                errmsg = ""
                for i in range(len(QuizfieldName)):
                    if QuizfieldValues[i].strip() == "":
                        errmsg += ("Answer is a required field.")
                if errmsg == "":
                    break  # no problems found
                QuizfieldValues = multenterbox(errmsg, QuizWintitle, QuizfieldName, QuizfieldValues)

            #Check valid input (that is, a fraction or number)
            while 1:
                input = clear_whitespace(QuizfieldValues[0])

                #incase the answer is number, includes negative.
                if isdigit(input):
                    pass
                else:
                    # incase the answer is fraction
                    Expression = re.compile(r'(?:-)?(\d+)/(\d+)').match(input)

                    if Expression == None:
                        msgbox("Wrong stuff you put into.", title="Error")
                        break
                    else:
                        pass

                # Check answer
                answer = operator.add(Fraction(int(fx), int(fy)), Fraction(int(sx), int(sy)))

                # Complete correct
                if str(answer) == QuizfieldValues[0]:
                    msgbox("Your answer is correct.", title="Congratulations!")
                    break
                # Partial Correct
                elif Fraction(answer) == Fraction(QuizfieldValues[0]):
                    msgbox("Nmmm not quiet, but close. The correct answer is " + str(QuizfieldName[0]) + str(answer),
                           title="So Close!")
                    break
                else:
                    msgbox("Wrong Answer my friend.", title="Sad")
                    break

        #if picked ' - '
        if QuizChoice == QuizWinchoice[1]:
            #Set Interface value
            #generate Random number
            fx = random.randint(-15, 15)
            fy = random.randint(-15, 15)
            while fy == 0: #in case the denominator gets 0
                fy = random.randint(-15, 15)
            sx = random.randint(-15, 15)
            sy = random.randint(-15, 15)
            while sy == 0: #in case the denominator gets 0
                sy = random.randint(-15, 15)

            QuizWinmsg = "Solve the fractions below: "
            QuizWintitle = "Solve fraction"
            QuizfieldName = [str(fx) + "/" + str(fy) + " - " + str(sx) + "/" + str(sy) + " = "]

            QuizfieldValues = multenterbox(QuizWinmsg, QuizWintitle, QuizfieldName)

            #Check button
            if QuizfieldValues:
                pass
            else:
                break
            # Check if the entry field is empty
            while 1:
                if QuizfieldValues == None:
                    break
                errmsg = ""
                for i in range(len(QuizfieldName)):
                    if QuizfieldValues[i].strip() == "":
                        errmsg += ("Answer is a required field.")
                if errmsg == "":
                    break  # no problems found
                QuizfieldValues = multenterbox(errmsg, QuizWintitle, QuizfieldName, QuizfieldValues)

            # Check valid input (that is, a fraction or number)
            while 1:
                input = clear_whitespace(QuizfieldValues[0])

                # incase the answer is number, includes negative.
                if isdigit(input):
                    pass
                else:
                    # incase the answer is fraction
                    Expression = re.compile(r'(?:-)?(\d+)/(\d+)').match(input)

                    if Expression == None:
                        msgbox("Wrong stuff you put into.", title="Error")
                        break
                    else:
                        pass

                # Check answer
                answer = operator.sub(Fraction(int(fx), int(fy)), Fraction(int(sx), int(sy)))

                # Complete correct
                if str(answer) == QuizfieldValues[0]:
                    msgbox("Your answer is correct.", title="Congratulations!")
                    break
                # Partial Correct
                elif Fraction(answer) == Fraction(QuizfieldValues[0]):
                    msgbox("Nmmm not quiet, but close. The correct answer is " + str(QuizfieldName[0]) + str(answer),
                           title="So Close!")
                    break
                else:
                    msgbox("Wrong Answer my friend.", title="Sad")
                    break


        #if picked ' * '
        if QuizChoice == QuizWinchoice[2]:
            #Set Interface value
            #generate Random number
            fx = random.randint(-15, 15)
            fy = random.randint(-15, 15)
            while fy == 0: #in case the denominator gets 0
                fy = random.randint(-15, 15)
            sx = random.randint(-15, 15)
            sy = random.randint(-15, 15)
            while sy == 0: #in case the denominator gets 0
                sy = random.randint(-15, 15)

            QuizWinmsg = "Solve the fractions below: "
            QuizWintitle = "Solve fraction"
            QuizfieldName = [str(fx) + "/" + str(fy) + " * " + str(sx) + "/" + str(sy) + " = "]

            QuizfieldValues = multenterbox(QuizWinmsg, QuizWintitle, QuizfieldName)

            #Check button
            if QuizfieldValues:
                pass
            else:
                break
            # Check if the entry field is empty
            while 1:
                if QuizfieldValues == None:
                    break
                errmsg = ""
                for i in range(len(QuizfieldName)):
                    if QuizfieldValues[i].strip() == "":
                        errmsg += ("Answer is a required field.")
                if errmsg == "":
                    break  # no problems found
                QuizfieldValues = multenterbox(errmsg, QuizWintitle, QuizfieldName, QuizfieldValues)

            # Check valid input (that is, a fraction or number)
            while 1:
                input = clear_whitespace(QuizfieldValues[0])

                # incase the answer is number, includes negative.
                if isdigit(input):
                    pass
                else:
                    # incase the answer is fraction
                    Expression = re.compile(r'(?:-)?(\d+)/(\d+)').match(input)

                    if Expression == None:
                        msgbox("Wrong stuff you put into.", title="Error")
                        break
                    else:
                        pass

                # Check answer
                answer = operator.mul(Fraction(int(fx), int(fy)), Fraction(int(sx), int(sy)))

                # Complete correct
                if str(answer) == QuizfieldValues[0]:
                    msgbox("Your answer is correct.", title="Congratulations!")
                    break
                # Partial Correct
                elif Fraction(answer) == Fraction(QuizfieldValues[0]):
                    msgbox("Nmmm not quiet, but close. The correct answer is " + str(QuizfieldName[0]) + str(answer),
                           title="So Close!")
                    break
                else:
                    msgbox("Wrong Answer my friend.", title="Sad")
                    break

        #if choose return
        if QuizChoice == QuizWinchoice[3]:
            break

    #When Choose Quit
    if Choice == MainWinchoice[2]:
        msg = "Do you want to Exit?"
        title = "Please Confirm"
        if ccbox(msg, title):  # show a Continue/Cancel dialog
            sys.exit(0)  # user chose Continue
        else:  # user chose Cancel
            pass