import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt

data = pandas.read_csv('cost_revenue_clean.csv')  # read the data
print(data)  # print the data
print(data.describe())  # print the data description

x = DataFrame(data, columns=['production_budget_usd'])  # get the production budget
y = DataFrame(data, columns=['worldwide_gross_usd'])  # get the worldwide gross

# print(x)
# print(y)

plt.figure(figsize=(10, 6))  # set the figure size
plt.scatter(x, y, alpha=0.3)  # plot the data
plt.title('Film Cost vs Global Revenue')  # set the title
plt.xlabel('Production Budget $')  # set the x label
plt.ylabel('Worldwide Gross $')  # set the y label
plt.ylim(0, 3000000000)  # set the y limit
plt.xlim(0, 450000000)  # set the x limit
print(plt.show())  # show the plot

