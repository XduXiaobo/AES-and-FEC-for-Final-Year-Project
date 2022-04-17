import random
from reedsolo import RSCodec, ReedSolomonError
import numpy as np
from numpy.core.fromnumeric import mean
import os
#def access_bit(data, num):
 #   base = int(num // 8)
 #   shift = int(num % 8)
 #   return (data[base] & (1<<shift)) >> shift
#Try not to exceed 255
FRAME_SIZE = 255
DATA_PAYLOAD = 239

fl = '100h'
readPath = f'{fl}.jpg.enc'
writePath = f'{fl}_generated.txt'
#writePath2= f'{fl}_generatedbit.txt'
#Open the input file
fin = open(readPath, "rb")

#Open the output file
fout = open(writePath, "wb")
#fout2 = open(writePath2, "w")


#Create the file to be transmitted

rsc = RSCodec(FRAME_SIZE-DATA_PAYLOAD)
for i in range(int(os.stat(readPath).st_size/DATA_PAYLOAD)+1):
#for i in range(int(os.stat(readPath).st_size/FRAME_SIZE)+1):
    
    data = fin.read(DATA_PAYLOAD)
    dataEncoded = rsc.encode(data)
    fout.write(dataEncoded)
    #print(dataEncoded)

    #bin=(np.array([access_bit(dataEncoded,n) for n in range(len(dataEncoded)*8)]))
    #bin='\n'.join('%s' %id for id in bin)
    #print(bin)
    #fout2.write(bin)
    
    #print(str_2_bin(dataEncoded))
#bin=np.array([access_bit(data,i) for i in range(len(data)*8)])
#print(np.array([access_bit(dataEncoded,i) for i in range(len(dataEncoded)*8)]))

