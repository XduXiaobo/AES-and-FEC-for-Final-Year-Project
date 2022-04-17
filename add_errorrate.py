def access_bit1(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data[base] & (1<<shift)) >> shift
#def str_2_bin1212121(str):
  #  """
  #  字符串转换为二进制
 #   """
#    return ''.join([bin(ord(c))[2:].zfill(8).replace('0b', '') for c in str])

import os
import numpy as np
#from reedsolo import RSCodec, ReedSolomonError
#Try not to exceed 255
#FRAME_SIZE = 255
#DATA_PAYLOAD = 239


fl = '100h'
#readPath = f'{fl}.jpg.enc'
writePath = f'{fl}_generated1.txt'
readPath=f'{fl}_generated.txt'
writePath2= f'{fl}_generatedbit.txt'

#Open the input file
fin = open(readPath, "rb")

#Open the output file
fout = open(writePath, "wb")
fout2 = open(writePath2, "w")


data=fin.read()
bin=(np.array([access_bit1(data,n) for n in range(len(data)*8)]))

bin='\n'.join('%s' %id for id in bin)
fout.write(data)
fout2.write(bin)

