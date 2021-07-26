import os, random
from random import sample

#Checking dir to see if we have to change it to the targeted one
dir_check= os.getcwd()
print("Current path is: ",dir_check)

#Changing current dir to the one we want to read our files from
path= 'E:\\Epsilon AI (CDSP)\\16-07-2021\\GCR\\Thanos Project\\Universe'
os.chdir(path)
dir_check= os.getcwd()
print('New path is: ',dir_check)

#Checking how many files in this folder using (len())
files_check= os.listdir(path)
print('You have: ', len(files_check))

#Removing half of the universe randomly
'''
for files in sample(files_check,25):
    os.remove(files)
'''

#Checking how many files is now in the universe
print('Now you have {} files'.format(len(files_check)))
