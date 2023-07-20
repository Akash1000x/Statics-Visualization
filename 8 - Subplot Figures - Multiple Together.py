
import matplotlib.pyplot as plt

f = open('salesdata2.csv','r')
salefile = f.readlines()

sale_list = []
s_list = []
c_list = []

for records in salefile:
    sale, cost = records.split(sep=',')
    s_list.append(int(sale))
    c_list.append(int(cost))
    
sale_list.append(s_list)
sale_list.append(c_list)

plt.subplot(2,2,1)
plt.title("Sales Vs Cost")
plt.xlabel("Sale")
plt.ylabel("Cost")
plt.scatter(s_list,c_list)

plt.subplot(2,2,2)
plt.title("Box Plot of Sales")
plt.ylabel("USD")
plt.boxplot(sale_list)
plt.show()

plt.subplot(2,2,3)
plt.title("Histogram of Sales")
plt.ylabel("USD")
plt.hist(s_list, bins=5, rwidth=0.9)

x_days  = [1,2,3,4,5]
y_price1 = [9,9.5,10.1,10,12]

plt.subplot(2,2,4)
plt.title("Stockprice History")
plt.ylabel("Price")
plt.xlabel("Day")
plt.plot(x_days, y_price1)

plt.tight_layout()

plt.savefig('01subplot.png')

plt.show()







