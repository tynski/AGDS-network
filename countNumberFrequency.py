def countNumberFrequency(numberList):
    valueandCount = {}
    for newNumber in numberList:
        if newNumber in valueandCount:
            valueandCount[newNumber] += 1
        else:
            valueandCount[newNumber] = 1
    return valueandCount
