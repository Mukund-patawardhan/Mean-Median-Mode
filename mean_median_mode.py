import csv
from collections import Counter

newData = []
fileData = []

def getMean():
    n = len ( newData )
    total = 0

    for num in newData :
        total = total + num

    mean = total / n

    print( "Mean is " + str(mean) )


def getMedian():
    n = len(newData)

    newData.sort()

    if n % 2 == 0 :
        firstNum = float ( newData[ ( n // 2 ) - 1 ] )
        secondNum = float( newData[( ( n // 2 ) + 1 ) - 1 ] )

        median = ( firstNum + secondNum ) / 2

    else :
        median = float ( newData[ ( ( n + 1 ) // 2 ) - 1 ] )

    print( "Median is " + str ( median ) )


def getMode():
    data = Counter(newData)

    modeDataForRange = {
        "75 - 85":0,
        "85 - 95":0,
        "95 - 105":0,
        "105 - 115":0,
        "115 - 125":0,
        "125 - 135":0,
        "135 - 145":0,
        "145 - 155":0,
        "155 - 165":0,
        "165 - 175":0,
    }

    for height,occurence in dict.items(data):
        if 75 < float(height) < 85 :
            modeDataForRange["75 - 85"] +=occurence 
        elif 85 < float(height) < 95 :
            modeDataForRange["85 - 95"] +=occurence
        elif 95 < float(height) < 105 :
            modeDataForRange["95 - 105"] +=occurence 
        elif 105 < float(height) < 115 :
            modeDataForRange["105 - 115"] +=occurence 
        elif 115 < float(height) < 125 :
            modeDataForRange["115 - 125"] +=occurence 
        elif 125 < float(height) < 135 :
            modeDataForRange["125 - 135"] +=occurence 
        elif 135 < float(height) < 145 :
            modeDataForRange["135 - 145"] +=occurence 
        elif 145 < float(height) < 155 :
            modeDataForRange["145 - 155"] +=occurence 
        elif 155 < float(height) < 165 :
            modeDataForRange["155 - 165"] +=occurence 
        elif 165 < float(height) < 175 :
            modeDataForRange["165 - 175"] +=occurence 

    modeRange , modeOccurence = 0 , 0

    for range,occurence in dict.items(modeDataForRange):
        if occurence > modeOccurence:
            modeRange , modeOccurence = [int ( range.split( " - " ) [0] ) , int ( range.split( " - " ) [1] )] , occurence
        
    mode = float ( (modeRange[0] + modeRange[1]) / 2)

    print (f"Mode is " + str(mode))


with open (r'SOCR-HeightWeight.csv',newline='') as f :
    reader = csv.reader(f)
    fileData = list ( reader )

fileData.pop(0)

for i in range (len (fileData) ) :
    n_num = fileData[i][2]
    newData.append(float(n_num))

print(newData)

getMean()
getMedian()
getMode()