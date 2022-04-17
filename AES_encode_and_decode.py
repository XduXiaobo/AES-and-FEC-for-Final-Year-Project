#Importing Stuff
#encoding='ascii'
from Crypto.Cipher import AES
import io
import PIL.Image
from tkinter import *
import os
import time
import random
import string
from Crypto.Random import get_random_bytes
#long running
#do something other
#Private Stuff
#key = b'0000000000111111' #Todo Enter a Key(Like a password only) Here of Length 16 (Both Key and ivb required keep both safely and securely)
iv = b'0000000000111111' #Todo Enter a ivb (Like a password only) Here of Length 16 (Both Key and ivb required keep both safely and securely)


cwd_original_1=os.getcwd()

cwd_original=os.path.join(cwd_original_1,"Encrypted")
cwd_original_decrypt=os.path.join(cwd_original_1,"Decrypted")
#Encrypting Image
def encrypt_image():
    start = time.time()
    try:
        os.mkdir(os.path.join(cwd_original_1,"Encrypted"))
    except:
        pass
    global key,iv,entry_for_folder,root
    file_path=str(entry_for_folder.get())
    if(file_path=="" or file_path[0]==" "):
        file_path=os.getcwd()
    files=[]
    # r=root, d=directories, f = files
    for r, d, f in os.walk(file_path):
        for file in f:
            file_str=file.lower()
            if((".jpg" in file_str or ".png" in file_str) and ('.enc' not in file_str)):
                direc = os.path.split(r)
                cwd=os.path.join(cwd_original,direc[-1])
                try:
                    os.mkdir(cwd)
                except:
                    pass #Chill
                input_file = open((os.path.join(r,file)),"rb")
                input_data = input_file.read()
                input_file.close()
               # key = get_random_bytes(len(input_data))
               # print(key)
                #print(len(input_data))
                l_input=len(input_data)/16+2
                #print(l_input)
                l_input=int(l_input)
                keystore=''
                enc_data=b''
                print(len(input_data))
                for i in range(1,l_input):
                    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
                    key = bytes(ran_str,'ascii')
                    keystore=keystore+ran_str;
                    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
                    if i < l_input:
                        enc_data = enc_data+cfb_cipher.encrypt(input_data[(i-1)*16:i*16])
                    if i == l_input:
                        enc_data = enc_data+cfb_cipher.encrypt(input_data[(i-1)*16:len(input_data)])
                    print(i)
                fh=open(os.path.join(cwd,file)+".enckey.txt",'w')
                fh.write(keystore)
                fh.close()
                print(keystore)
                enc_file = open(os.path.join(cwd,file)+".enc", "wb")
                enc_file.write(enc_data)
                enc_file.close()
    root.destroy()
    root = Tk()
    root.title("Encryption Successfully Done")
    root.geometry("400x200")
    label = Label(text="Encryption Successfully Done", height=50, width=50, font=(None, 15))
    label.pack(anchor=CENTER, pady=50)
    end = time.time()
    print(end-start)
    root.mainloop()
#Decrypting Image
def decrypt_image():
    start = time.time()
    try:
        os.mkdir(os.path.join(cwd_original_1, "Decrypted"))
    except:
        pass
    global iv,entry_for_folder,root
    file_path = str(entry_for_folder.get())
    if (file_path == "" or file_path[0] == " "):
        file_path = os.getcwd()
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(file_path):
        for file in f:
            file_str=file.lower()
            if ('.enc' in file_str) and ('.txt' not in file_str):
                direc = os.path.split(r)
                cwd = os.path.join(cwd_original_decrypt, direc[-1])
                try:
                    os.mkdir(cwd)
                except:
                    pass #Chill
                enc_file2 = open(os.path.join(r,file),"rb")
                enc_data2 = enc_file2.read()
                enc_file2.close()
                key_file2 = open(os.path.join(r,file+"key.txt"),"r")
                key_data2 = key_file2.read()
                key_file2.close()
                l_input2=len(enc_data2)/16+1
                l_input2=int(l_input2)
                plain_data=b''
                for i in range(1,l_input2+1):
                    key=bytes(key_data2[(i-1)*16:i*16],'ascii')
                    cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
                    if i < l_input2:
                        plain_data = plain_data+cfb_decipher.decrypt(enc_data2[(i-1)*16:i*16])
                    if i == l_input2:
                        plain_data = plain_data+cfb_decipher.decrypt(enc_data2[(i-1)*16:len(enc_data2)])
                    print(i)
                imageStream = io.BytesIO(plain_data)
                imageFile = PIL.Image.open(imageStream)
                file_str=file.lower()
                if(".jpg" in file_str):
                    imageFile.save(((os.path.join(cwd,file))[:-8])+".JPG")
                elif(".png" in file_str):
                    imageFile.save(((os.path.join(cwd, file))[:-8]) + ".png")

    root.destroy()
    root = Tk()
    root.title("Decryption Successfully Done")
    root.geometry("400x200")
    label = Label(text="Decryption Successfully Done",height=50, width=50,font=(None, 15))
    label.pack(anchor=CENTER,pady=50)
    end = time.time()
    print(end-start)
    root.mainloop()



#Tkinter Stuff

root=Tk()

root.title("Simple AES Encryption and Decryption of JPG Images")

folder_directory_label=Label(text="Enter the Folder Directory")
folder_directory_label.pack()

entry_for_folder=Entry(root)
entry_for_folder.pack()


encrypt=Button(text="Encrypt All",command=encrypt_image)
encrypt.pack()
label=Label(text="Leave Blank for Current Working Directory")
label.pack()
decrypt=Button(text="Decrypt All",command=decrypt_image)
decrypt.pack()



root.mainloop()


# All good