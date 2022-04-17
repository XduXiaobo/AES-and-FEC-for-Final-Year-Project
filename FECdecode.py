from reedsolo import RSCodec, ReedSolomonError
from Crypto.Cipher import AES
import io
import PIL.Image
from tkinter import *
import os
import time
import random
import string
from Crypto.Random import get_random_bytes
from bitstring import BitArray

#Try not to exceed 255
FRAME_SIZE = 255
DATA_PAYLOAD = 239



#fl = 'ShrekLadder_FEC'
fl = '100h'
#readPath = f'{fl}_generated.jpg.enc'
readPath = f'{fl}_mid.txt'
writePath = f'{fl}_fin.txt'
#Open the input file
fin = open(readPath, "rb")
fout = open(writePath, "wb")

#Open the output file

rsc = RSCodec(FRAME_SIZE-DATA_PAYLOAD)
for i in range(int(os.stat(readPath).st_size/DATA_PAYLOAD)+1):
    #for i in range(int(os.stat(readPath).st_size/FRAME_SIZE)+1):
    
    dataIn = fin.read(FRAME_SIZE)

    de = rsc.decode(dataIn)
    #print(de)
    fout.write(de[0])

    
