import os

# enter file input name
mentionMap = 'newMentionMap.txt'

# get Current path of this file
currentPath = os.getcwd()

# Start reading the file in separate lines
with open(currentPath + '/' + mentionMap) as f:
    lines = f.readlines()
    # stripping the newline character
    lines = [x.strip() for x in lines]

#this scan will check whether there are any duplicate lines

#an empty list to add the unique lines
newLines = []

for line in lines:
    if line not in newLines:
        newLines.append(line)

print(str(len(lines) - len(newLines)) + ' lines have been removed')

#write these values to the final file

# create new file to add non empty entries
finalFile = open('intermediateMentionMap.txt', 'w')

for writeLine in newLines:
    print(writeLine, file=finalFile)
finalFile.close()

#now let's create two lists with the doc names and references separately
docList = []
referenceList = []

for newLine in newLines:
    docList.append(newLine.split(';')[0])
    referenceList.append(newLine.split(';')[1])

finalList = []
#now check for duplicate document entries and merge the references with a Union operation

length = len(docList)
checkedList = []
counter = 0
for i in range(0 , length):
    counter = counter + 1
    print(str(counter) + '/' + str(length))

    if i in checkedList:
        continue
    else:
        checkedList.append(i)

        keyDocument = docList[i]
        indices = [i for i, x in enumerate(docList) if x == keyDocument]

        if len(indices) == 1:
            finalList.append(docList[indices[0]] + ';' + referenceList[indices[0]])
            continue
        else:
            unionList = []
            for index in indices:
                unionList = list(set(unionList).union(referenceList[index].split(',')))
                if index not in checkedList:
                    checkedList.append(index)
            finalList.append(docList[indices[0]] + ';' + ",".join(unionList ))

print("success")

# create new file to add non empty entries
finalFile = open('finalMentionMap.txt', 'w')

for finalLine in finalList:
    print(finalLine, file=finalFile)
finalFile.close()