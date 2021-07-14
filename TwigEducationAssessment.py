def GroupArrayElements(RecievedArray, DivisableNumber):
    """
    GroupArrayElements(Array[INT Array], DivisableNumber[INT]): Divides 'RecievedArray' by 'DivisableNumber', if Odd 'RecievedArray(Count)' returns 
    """
    Divisor = (len(RecievedArray) / DivisableNumber)
    Remainder = (len(RecievedArray) % DivisableNumber)
    Current_Position = 0
    Return_Array = []

    #Determine Position of Range to Break 'RecievedArray' into Chucks
    if (Remainder == 0) or (Divisor < DivisableNumber):
        RangePosition = DivisableNumber
    elif (Remainder != 0):
        RangePosition = DivisableNumber + 1

    #Break 'RecievedArray' into Batches, by Specifiying Batch Range of 'Template_Array' and Extacting from 'RecievedArray' 
    for i in range(0, RangePosition):
        if (Current_Position + round(Divisor))>len(RecievedArray):
            Template_Array = [x for x in range(Current_Position, len(RecievedArray))]
        else:
            Template_Array = [x for x in range(Current_Position, (Current_Position + round(Divisor)))]
        Return_Array.append([RecievedArray[i] for i in Template_Array])
        Current_Position = Current_Position + (round(len(RecievedArray) / DivisableNumber))

    return Return_Array


print("---Start---")
TestingArray = GroupArrayElements([1,2,3,4,5], 3)
print(TestingArray)
TestingArray = GroupArrayElements([1,2,3,4,5,6,7,8,9,10], 3)
print(TestingArray)
TestingArray = GroupArrayElements([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 4)
print(TestingArray)
TestingArray = GroupArrayElements([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 5)
print(TestingArray)
TestingArray = GroupArrayElements(['A','B', 'C', 'D', 'E'], 3)
print(TestingArray)
TestingArray = GroupArrayElements(['A','B'], 3)
print(TestingArray)
TestingArray = GroupArrayElements(['A','B'], 2)
print(TestingArray)
TestingArray = GroupArrayElements(['A','B'], 1)
print(TestingArray)
print("---End---")

