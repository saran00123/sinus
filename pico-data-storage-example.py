import machine
import utime
import os

#we will use the inbuilt LED as a file activity light
LED_FileWrite = machine.Pin(25,machine.Pin.OUT)
#Define a file name and a maximum size in bytes
LogFileName = "log.txt"
Max_File_Size = 100
     
#This writes whatever is passed to it to the file     
def WriteFile(passed):
    LED_FileWrite.value(1) #indicate writing to file, so don't power off
    log = open(LogFileName,"a") #open in append - creates if not existing, will append if it exists
    log.write(passed)
    log.close()
    LED_FileWrite.value(0)

#This returns the size of the file, or 0 if the file does not exist
def CheckFileSize():
    # f is a file-like object.
    try:
        f = open(LogFileName,"r") # Open read - this throws an error if file does not exist - in that case the size is 0
        f.seek(0, 2)
        size = f.tell()
        f.close()
        return size
    except:
        # if we wanted to know we could print some diagnostics here:
        #print("Exception - File does not exist?")
        return 0 


#This removes one line from the file by copying the whole file except the first line to a new file and then renaming it
def RemoveOneLine():
    LED_FileWrite.value(1) #indicate writing to file, so don't power off
    tmpName = LogFileName + '.bak'

    with open(LogFileName, 'r') as readFrom:   #open both files
        #print(readFrom.read(1)) #read the first line and throw it away. This moves the file handle on by 1 line.
        a = readFrom.readlines()
        print("a = ",a[26])
        # Now Read the rest of the lines from original file one by one and write them to the dummy file
        #for char in readFrom:
            #writeTo.write(char)
 #now close all the handles and swap the file names around.
    #readFrom.close()
    #writeTo.close()
    #os.remove(LogFileName)
    #os.rename(tmpName,LogFileName)
    #LED_FileWrite.value(0)
  

#We will just write an incrementing number to the file
number = 0

while True:
    #if(CheckFileSize() > Max_File_Size):
    RemoveOneLine()
    if(CheckFileSize() < Max_File_Size):
        stringToWrite = str(number) + "\r\n" #add a line feed/carriage return to ensure each number is on its own line in the file
        WriteFile(stringToWrite)
        number+=1
        print("writing..............")
        utime.sleep(1) #give a chance to break back in.
    else:
        print("storage full")
        utime.sleep(1)