"Load Data From The External File"
import numpy as np

np.genfromtxt('data.txt', delimiter=',')
# This will load data from 'data.txt' assuming it is a CSV file.
data = np.genfromtxt('data.txt', delimiter=',')
print(data)
#turn it into intergers(int32)
filedata = data.astype(np.int32)
print(filedata)

'''Boolean Masking and advanced Indexing'''

print(filedata > 50) #This will give True/False values

print(filedata[filedata > 50]) #This will give values greater than 50

a = np.any(filedata > 50 , axis = 0) #if any value greater than 50 in each column  
print(a)
b = np.all(filedata > 50 , axis = 1) #if all values greater than 50 in each row
print(b)
print("Now PRINTING C")
c = ((filedata > 50) & (filedata < 100)) #values between 50 and 100
print(c)
''' You can reverse the mask using ~ '''
print("Now PRINTING D")
d = (~((filedata > 50) & (filedata < 100))) #values NOT between 50 and 100
                 #OR
        # d = (~(c)) #Reversing c 
print(d)
