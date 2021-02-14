numList = []
initialInput = int(input())
for i in range(initialInput):
    num = int(input())
    if num >  -100000000:
        numList.append(num)
    else:
        break
numList = sorted(numList)
sizes = []
count = 0
for i in numList:
    if (i == max(numList)) or (i == min(numList)):
        continue
    else:
        leftSide = (i - numList[count]) / 2
        rightSide = ((i - numList[count + 2]) * -1) / 2
        total = round(leftSide + rightSide, 1)
        sizes.append(total)
        count += 1
print(min(sizes))

        

    
