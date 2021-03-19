def file_lengthy(FileName):
    with open(FileName) as OurFile:
        for Number, Line in enumerate(OurFile):
            pass
    return Number + 1


print("Number of lines in your file is: {}".format(file_lengthy("OurText.txt")))
