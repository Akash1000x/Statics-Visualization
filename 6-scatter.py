import matplotlib.pyplot as plt

f = open('salesdata2.csv','r')
data = f.readlines()

s_list = []
c_list = []

for records in data:
    sale,cost = records.split(',')
    s_list.append(int(sale))
    c_list.append(int(cost))

plt.title("Sales Vs Cost")
plt.xlabel("Sale")
plt.ylabel("Cost")

plt.scatter(s_list,c_list)
plt.show()