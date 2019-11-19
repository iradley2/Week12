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

def FindWordCount(list1, string):
    count = list1.count(string)
    return count

def ScoreFinder(list1, list2, string):
    lower_string = []
    for i in range(len(list1)):
        lower_string.append(list1[i].lower())
    string = string.lower()
    for i in range(len(list1)):
        if (string == lower_string[i]):
            print("OUTPUT",list1[i], "got a score of", list2[i])
            break
    else:
        print("OUTPUT player not found")
