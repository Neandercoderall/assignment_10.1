#CIS245-T302

# Nov 15, 2021

# Jeremy Dowlen


import os

template = "Directories"
print(template)




def createDirIfNotExist(dirName):
    isExist = os.path.exists(dirName)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(dirName)
        print("The new directory is created!")


def createFileInDir(dirName):
    save_path = './' + dirName
    name_of_file = input("What is the name of the file: ")
    completeName = os.path.join(save_path, name_of_file + ".txt")
    file1 = open(completeName, "w")
    toFile = input("Write what you want into the field")
    file1.write(toFile)
    file1.close()
    return completeName


def readFile(completeName):
    a_file = open(completeName, "r")
    lines = a_file.readlines()
    for line in lines:
        print(line)
    a_file.close()


directoryName = input("What directory do you want to save your file in?")
createDirIfNotExist(directoryName)
completeName = createFileInDir(directoryName)
readFile(completeName)


















