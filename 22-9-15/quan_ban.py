import struct

input_file = open("test.txt","r")

output_file = open('test.txt','wb')

for line in input_file :
    line = line.encode('gbk')
    for i in range(0,len(line)):
        if 0x80 & line[i] == 0 :
            Quan = struct.pack('BB',0xa3,line[i]+128)
            # To be continue ...

