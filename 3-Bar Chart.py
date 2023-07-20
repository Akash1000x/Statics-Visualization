import matplotlib.pyplot as plt

x_cities = ['NewYork', 'London', 'Dubai', 'New Delhi','Tokyo']
y_temp = [75,65,105,98,90]

plt.title('Tempreture Varition')
plt.xlabel('Cities')
plt.ylabel('Temprature')

plt.bar(x_cities,y_temp, color = 'hotpink')

plt.show()