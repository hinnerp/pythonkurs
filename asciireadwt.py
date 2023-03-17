
#import

import os
import time
import argparse
import numpy as np

#parser

parser = argparse.ArgumentParser(description ='Dieses Script öffnet eine Asciifile mit Werten in zwei Spalten. Parameter: -infile und -mode (mögliche Modi: r oder c)')
parser.add_argument('-infile', type = str, help='input file')
parser.add_argument('-mode', choices =['r', 'c'], help='mode if data is written in rows or columns')

args = parser.parse_args()
print(args.infile)
print(args.mode)
##

print('')
print(' @@@@@ ')
print(' |o o| ')
print(' \ - / ')
print('  |_|  ')
print('')

#variablen

file1 = []
testwert = 250 #schwellenwert für intensity-filter
trennzeichen = ',' #trennzeichen output
trenninput = ' ' #trennzeichen input

# welcher input?

if args.infile == None:
    print('None')
    pedata = open(r'C:\Users\Hinner\Downloads\pointcloud1_small.txt', 'r')
else:
    inputfile = args.infile
    pedata = open(inputfile, 'r')      

data = list(pedata)#[:1000]             #falls nicht alle Zeilen verarbeitet werden sollen

#define textdatei schreiben

def totext(array,name):
    text = open(name,'w')
    for lines in array:
        helpstring = ''
        for element in lines:
            helpstring = helpstring + trennzeichen + str(element)
            helpstring = helpstring.strip(trennzeichen)
        text.write(helpstring +'\n')
    text.close()

#textdatei in array schreiben

for line in data:
    line = line.expandtabs(1) #tabs umwandeln
    line = line.strip()
    sepline = line.split(trenninput)
    row = []
    for element in sepline:
        value = float(element)
        row.append(value)
        
    file1.append(row)
    
file1array = np.array(file1)

print('---------------------------------------')

#arrays in textdateien schreiben

if args.mode == 'r':
    file1arrayt = file1array.transpose()
    totext(file1arrayt,'pointarraytrans.txt')
elif args.mode == 'c':
    totext(file1array, 'pointarray.txt')
else:
    print('failed successfully')

#array erstellen, relevante Werte übernehmen und neue Datei schreiben

count = 0
for things in file1array:
    if things[3] <= testwert:
        count = count + 1

newarray = np.zeros((count,len(file1array[1])))
posz = 0

for things in file1array:
    if things[3] <= testwert:
        posy = 0
        for position in things:
            newarray[posz][posy] = position
            posy = posy + 1
        newarray[posz][3] = newarray[posz][3]**2
        posz = posz + 1


totext(newarray, 'pointcloud.txt')

print('insgesamt ', (len(file1array)-len(newarray)) ,' Punkte entfernt')

print('')
print(' /^^^\ ')
print(' @o-o@ ')
print(' \ - / ')
print('  |_|  ')
print('')

time.sleep(5)
