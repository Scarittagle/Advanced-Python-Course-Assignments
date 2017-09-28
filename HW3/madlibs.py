#Assignment3
#WEIWEI SU
#U17420699
#Last Modify: 9-17-2017
#Filename: madlibs.py

def mad_libs(inputname, outputname):
        #define properties
        adjective = input("Enter a adjective: ")
        noun = input("Enter a noun: ")
        verb = input("Enter a verb: ")
        noun1 = input("Enter a noun: ")
        
        #READ INPUT FILE
        inputstring = open(inputname,"r")
        string = inputstring.read()

        #Check string and replace words
        newstr = string.replace("ADJECTIVE", adjective)
        newstr = newstr.replace("VERB", verb)
        newstr = newstr.replace("NOUN", noun, 1)
        newstr = newstr.replace("NOUN", noun1)

        #Output to a new text file
        outputstring = open(outputname, "w")
        outputstring.write(newstr)

        #Close All Files
        inputstring.close()
        outputstring.close()

mad_libs("inputname.txt", "outputname.txt")