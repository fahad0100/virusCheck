import os,sys,time,hashlib

from hashlib import md5

class style():
    RED = lambda x: '\033[31m' + str(x)
    WHITE = lambda x: '\033[37m' + str(x)



file_list=[]
hashArray=[]
virsArray=[]
getVirus=[]

root_dir="C:/"  # path dir


# get hash for dir 
def Hash_md5(filename):
    md5 = hashlib.md5()
    try:
        with open(filename,'rb') as f: 
            for chunk in iter(lambda: f.read(8192), b''): 
                md5.update(chunk)
        return md5.hexdigest()
    except:
        print("there is problem in orgeal hash")
        pass





try:
    fileme = open("data/dir.txt", "w") # get the all sub the  dir 
    hashed = open("data/hashOrgnole.txt", "w") # get 
    print(" Start Collection ...")
    time.sleep(4)
except IOError:
    print('error dir ')

else:
    with fileme:
        for subdir,dirs,files in os.walk(root_dir):
            for file in files:
                file_path=subdir + os.sep + file
                if(file_path.endswith(".exe") or file_path.endswith(".dll") or file_path.endswith(".bat") or file_path.endswith(".cmd") or file_path.endswith(".pif") or file_path.endswith(".scr")):
                    print("{}".format(file_path))
                    orjnel = Hash_md5(file_path)
                    orjnel = Hash_md5(file_path)
                    if orjnel != None:
                        file_list.append(file_path) # add in arr
                        fileme.write(file_path) # add in file 
                        fileme.write("\n") # new line 
                        hashArray.append(orjnel) # add in arr
                        hashed.write(orjnel) # add in file 
                        hashed.write("\n") # new line 
    fileme.close()
    hashed.close()





try:
# Using readlines() 
    file1 = open('viruses.txt', 'r') 
    Lines = file1.readlines() 
    for line in Lines: 
        viresHash = str(line.strip())
        virsArray.append(viresHash)
except:
    print("Error")



VirusW = open("data/dirForVirus.txt", "w")
i=0
count = len(file_list)
print("count {}".format(count))
print(" Start Scan ...")
time.sleep(2)

while i < count: 
    for virus in virsArray:
        cheak = hashArray[i]
        if cheak == virus :

            print("------------------Bad-------------------------")
            print(file_list[i])
            print(hashArray[i])
            getVirus.append(file_list[i])
            VirusW.write(file_list[i])
            print("-------------------------------------------")

    
    i+=1
VirusW.close()
print("Dir cheak {}".format(len(file_list)))
print("original hash get {}".format(len(hashArray)))
print("virus hash uploaded {}".format(len(virsArray)))
print("Found vires {}".format(len(getVirus)))



