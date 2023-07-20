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

plt.subplot(2,3,1)
plt.title("Sales Vs Cost")
plt.xlabel("Sale")
plt.ylabel("Cost")
plt.scatter(s_list,c_list,marker='*',s=100,color = 'r')

plt.subplot(2,3,2)
plt.title("Box Plot of Sales")
plt.ylabel("USD")
plt.boxplot(sale_list,                                               \
            patch_artist=True,                                       \
            boxprops=dict(facecolor='g', color='r', linewidth=2),    \
            whiskerprops=dict(color='r', linewidth=2),               \
            medianprops=dict(color='w', linewidth=1),                \
            capprops=dict(color='k', linewidth=2),                   \
            flierprops=dict(markerfacecolor='r', marker='o', markersize=7))

plt.subplot(2,3,3)
plt.title("Histogram of Sales")
plt.ylabel("USD")
plt.hist(s_list, bins=5, rwidth=0.9, color='c')

x_days  = [1,2,3,4,5]
y_price1 = [9,9.5,10.1,10,12]

plt.subplot(2,3,4)
plt.title("Stockprice History")
plt.ylabel("Price")
plt.xlabel("Day")
plt.plot(x_days, y_price1, color='green', marker='o', markersize=10, linewidth=3, linestyle='--')

x_cities = ['NewYork', 'London', 'Dubai', 'New Delhi','Tokyo']
y_temp = [75,65,105,98,90]

plt.subplot(2,3,5)
plt.title("Temperaure Variation")
plt.xlabel("Cities")
plt.ylabel("Temperature")
plt.xticks(rotation='vertical')
plt.bar(x_cities,y_temp, color=['r','g', 'c', 'y', 'm'])

# tight_layout to avoid overlap
plt.tight_layout()


plt.show()
