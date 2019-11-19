def PrintOutput(string):
    print("OUTPUT", string)

def LoadFile(string):
    contents = open(string)
    contents = contents.read()
    contents.split("\n")
    return contents

def UpdateString (string1, string2, index):
    new_string = string1[:index] + string2 + string1[index+1:]
    print(new_string)
