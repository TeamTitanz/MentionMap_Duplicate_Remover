import os
import fileinput

# enter file input name
mentionMap = 'newMentionMap.txt'

#the file name of the hash check file
hashCheck = 'dup.txt'

# get Current path of this file
currentPath = os.getcwd()

# Start reading the file in separate lines
with open(currentPath + '/' + hashCheck) as hashfile:
    lines = hashfile.readlines()
    # stripping the newline character
    lines = [x.strip() for x in lines]

current = ""
count = 0
docList = []
replacementList = []
for hash in lines:
    print(str(count) + '/' + str(len(lines)))
    current = hash.split(" ")[0]
    count = count + 1

    docList.append(hash.split('.')[1].split('/')[1])

    if count==len(lines) or lines[count].split(" ")[0] == current :
        continue

    else:
        if len(docList) == 1:
            replacementList.append(docList[0])
            continue
        else:
            mainDocName = docList[0]
            replacements = ','.join(docList[1:])
            # for i in range(1 , len(docList)):
                # f = open(currentPath + '/' + mentionMap, 'r')
                # filedata = f.read()
                # f.close()
                #
                # newdata = filedata.replace(docList[i], mainDocName)
                #
                # f = open(currentPath + '/' + mentionMap, 'w')
                # f.write(newdata)
                # f.close()
            docList = []
            replacementList.append(mainDocName + ':' + replacements)


# create new file to add non empty entries
f = open('backwardsMap.txt', 'w')

for line in replacementList:
    print(line, file=f)

f.close()
# test ='0008ff4af56a853493844eebdc186046  ./0010001200.txt'
# print(test.split('.')[1].split('/')[1])
# print(test.split(" ")[0])

