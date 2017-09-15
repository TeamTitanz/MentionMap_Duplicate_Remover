import os
import fileinput

# enter file input name
mentionMap = 'finalMentionMap.txt'

# get Current path of this file
currentPath = os.getcwd()

# Start reading the file in separate lines
with open(currentPath + '/' + mentionMap) as f:
    lines = f.readlines()
    # stripping the newline character
    lines = [x.strip() for x in lines]

#now let's create two lists with the doc names and references separately
docList = []
referenceList = []

for newLine in lines:
    docList.append(newLine.split(';')[0])
    referenceList.append(newLine.split(';')[1])

finalList = []
for i in range(0,len(docList)):
    document = docList[i]
    reference = referenceList[i].split(',')
    reference = list(set(reference))

    if document in reference:
        indices = [i for i, x in enumerate(reference) if x == document]
        templist = []
        for j in range (0, len(reference)):
            if j not in indices:
                templist.append(reference[j])
        finalList.append(document + ';' + ','.join(templist))


    else:
        finalList.append(document + ';' + ','.join(reference))

print("success")

# create new file to add non empty entries
finalFile = open('lastMentionMap.txt', 'w')

for finalLine in finalList:
    print(finalLine, file=finalFile)
finalFile.close()