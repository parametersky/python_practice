
# split a string use custom strings
sSplit = " "

# how read a file
f = open("data.txt","r")
fr = open("result.txt","w")

def getTimeStamp(line):
    result1 = line.split(" ")
    result2 = result1[1].split(".")
    return result2[1]
def processLine(index, cline, exline):
    time1 = int(getTimeStamp(exline));
    time2 = int(getTimeStamp(cline));
    if time2 < time1:
        time2 = time2 + 1000;
    interval = time2 - time1;
    fr.write(str(index)+ " "+str(time2)+" "+str(time1)+" " +str(interval))  
    if interval > 20:
        print str(index)+" time interval is "+str(interval)

def main():
    linenumber = 1
    exLine = f.readline()
    while True:
        currentLine = f.readline()
        if currentLine:
            processLine(linenumber,currentLine,exLine)
            exLine = currentLine
            linenumber += 1
        else:
            break
    f.close()
print getTimeStamp("11-04 22:03:47.523  12469-13908/com.kcl.dfss W/Player: display done")
main()

