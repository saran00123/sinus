import machine
import utime

a0 = machine.ADC(26)
a1 = machine.ADC(27)
a2 = machine.ADC(28)

def repeat0():
    a=0
    i=0
    sum=0
    while i < 10 :
        a = a0.read_u16()
        sum = sum +a
        #print ("sum: ",sum)
        i+=1
    sum = (sum / 10000)
    return sum

def repeat1():
    a=0
    i=0
    sum=0
    while i < 10 :
        a = a1.read_u16()
        sum = sum +a
        #print ("sum: ",sum)
        i+=1
    sum = (sum / 10000)
    return sum

def repeat2():
    a=0
    i=0
    sum=0
    while i < 10 :
        a = a2.read_u16()
        sum = sum +a
        #print ("sum: ",sum)
        i+=1
    sum = (sum / 10000)
    return sum

while True:
    ar0 = repeat0()
    ar1 = repeat1()
    ar2 = repeat2()
    print("ADC:  ar0: ",ar0)
    print("ADC:  ar1: ",ar1)
    print("ADC:  ar2: ",ar2)
    print("-----------------------------------------------------")
    utime.sleep(2)
    
