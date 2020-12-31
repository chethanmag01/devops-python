import re
imfile = "dockerimages.txt"
acfile = "dockerrunningcontainers.txt"
rcfile = "dockerallcontainers.txt"

filesList = [imfile,acfile,rcfile]

data = {}

for fname in filesList:
    fp = open(fname,"r")
    opList= []
    for line in fp.readlines():
        #remove more tha 2 whitespaces
        line = re.sub('  +', ':', line)
        #remove any newline char
        line = re.sub('\n', '', line)
        #split all the fields and store in list
        infoList = line.split(":")
        #to avoid any empty list
        if len(infoList)>1:
            opList.append(infoList)
    #copy the list of list into dictionary
    data[fname] = opList

for doc,val in data.items():
    print(doc,val)
