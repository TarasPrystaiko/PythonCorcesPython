def main():
    print " This program reads from a file and then prints out the"
    print " line with the longest length the line ,or with the highest sum"
    print " of ASCII values , or the line with the greatest number of words"
    length()

def length():
    maxlength = 0
    maxlinetext = ""
    infile = open("30075165.txt","r")
    for line in infile:
        linelength = len(line)
        if linelength > maxlength:
            #If linelength is greater than maxlength value the new value is linelength
            maxlength = linelength
            maxlinetext = line
    print maxlinetext
    infile.close()