## THIS IS A WIP, DON'T RUN

import sys

#Global Variables
REGISTERS = ["A", "B", "C", "D"]
WRITE = ["1000","0100","0010","0001"]
READ = ["010", "001", "011", "100"] #Order is A, B, C, D

#Boolean to control if line numbers are printed
LINENUM = True

#main methods
def main(): #Main method
    file = getFileName() #gets file name from args
    allCommands = openFile(file) #opens the file

    binaryStrings = [] #creates new array to hold binary values
    for command in allCommands:
        binaryStrings.append(returnBinary(command))#populates binaryStrings

    print("\n\n")
    x=0
    for i in binaryStrings:
        printstring = ""
        if (LINENUM):
            printstring = str(x) + " | " + i
        else:
            printstring = i
        print(printstring)
        x+=1
    print("\n\n")

    return 0;

def getFileName(): #Returns filename from args. TODO: Should add more checks
    if (len(sys.argv)!=2):# If the input isn't "python compiler.py [filename]"
        print("Error 1")
        return 0;
    else:
        return sys.argv[1]
def openFile(filename): # Opens "filename" as a file
    linearray = []
    sourceFile = open(filename, "r")
    for line in sourceFile:
        linearray.append(line.upper().split()) #Ensures all the lines are upper case, then splits by space
    sourceFile.close()
    return linearray
def returnBinary(commandLine):
    opcode = commandLine[0]
    operands = commandLine[1:len(commandLine)] # rest of the array
    returnstring = ""

    if (opcode=="LD"):
        returnstring = ld(operands)
    else:
        print("Not LD")

    return returnstring


#Operations
def ld(operands): #LD
    # LD always has two arguments
    returnstring = "000 " #LD XX XX

    if (operands[0] in REGISTERS): #LD [REGISTER] XX
        writeregister = matchWriteRegister(operands[0])
        if (operands[1] in REGISTERS): #LD [REGISTER] [REGISTER]
            returnstring += "000 "  #subopcode
            returnstring += writeregister + " " #writeregister
            returnstring += matchReadRegister(operands[1]) #readregister
            returnstring += " 000 " #not used
            returnstring += "00000000" #empty constant
        elif (operands[1][0:1]=="&"): #LD [REGISTER] [RAM]
            returnstring += "010 " #subopcode
            returnstring += writeregister #writeregister
            returnstring += " 000" #readregister
            returnstring += " 000 " #not used
            returnstring += str(operands[1][1:len(operands[1])]) #RAM address
        else:
            returnstring += "011 " #subopcode
            returnstring += writeregister #writeregister
            returnstring += " 000" #readregister
            returnstring += " 000 " #not used
            returnstring += toBinary(operands[1]) #RAM address

    elif (operands[0][0:1]=="&"):## LD RAM [REGISTER]
        returnstring += "010 0000 "
        if (operands[1] in REGISTERS):
            returnstring += matchReadRegister(operands[1])
            returnstring += " 000 "
            returnstring += str(operands[0][1:len(operands[0])])
        else:
            returnstring += "Error: 4"

    return returnstring


#Support functions
def toHex(binary): #Converts binary number to Hex
    unformatted = hex(int(str(binary),2)) #Converts number to base 2, then turns into hex
    return unformatted[2:len(unformatted)-1] #Chops off the first two characters, '0x'
def toBinary(decimal): #Converts decimal into binary
    unformatted = bin(int(decimal))
    unformatted = unformatted[2:len(unformatted)-1] #Chops off the first two characters, '0b'
    while (len(unformatted)<8):
        unformatted = "0" + unformatted
    return str(unformatted)

def matchWriteRegister(register): #Returns binary for register write
    if (register=="A"): return WRITE[0]
    if (register=="B"): return WRITE[1]
    if (register=="C"): return WRITE[2]
    if (register=="D"): return WRITE[3]
    else: return "Error: 2"
def matchReadRegister(register): #Returns binary for register read
    if (register=="A"): return READ[0]
    if (register=="B"): return READ[1]
    if (register=="C"): return READ[2]
    if (register=="D"): return READ[3]
    else: return "Error: 3"

main()
