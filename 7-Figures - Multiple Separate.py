import matplotlib.pyplot as plt

f = open('salesdata2.csv','r')
data = f.readlines()

sale_list = []
s_list = []
c_list = []

for records in data:
    sale,cost = records.split(',')
    s_list.append(int(sale))
    c_list.append(int(cost))

sale_list.append(s_list)
sale_list.append(c_list)

plt.figure('My Scatter Plot')
plt.title("Sales Vs Cost")
plt.xlabel("Sale")
plt.ylabel("Cost")
plt.scatter(s_list,c_list)


plt.figure('My Boxplot')
plt.title("Box Plot of Sales")
plt.ylabel("USD")
plt.boxplot(sale_list)

plt.show()