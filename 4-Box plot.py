import matplotlib.pyplot as plt

f = open('salesdata.csv','r')
data = f.readlines()

list = []

for records in data:
    list.append(int(records))

plt.boxplot(list)
plt.show()