import matplotlib.pyplot as plt
# import numpy as np

file =open('agedata.csv','r') 
agefile = file.readlines()

agelist = []

for data in agefile:
    agelist.append(int(data))
# print(agelist)

bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.title("Age histogram")
plt.xlabel("Group")
plt.ylabel("Age")

plt.hist(agelist,bins,histtype='bar', rwidth=0.9)
plt.show()
    