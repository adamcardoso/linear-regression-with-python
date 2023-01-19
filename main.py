import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('cost_revenue_clean.csv')  # read the data
print(data)  # print the data
print(data.describe())  # print the data description

x = DataFrame(data, columns=['production_budget_usd'])  # get the production budget
y = DataFrame(data, columns=['worldwide_gross_usd'])  # get the worldwide gross

# print(x)
# print(y)

regression = LinearRegression()  # create the linear regression model
regression.fit(x, y)  # fit the model
# Slope Coefficient:
print('Slope Coefficient: ', regression.coef_)  # print the slope coefficient
print('Intercept: ', regression.intercept_)  # print the intercept

plt.figure(figsize=(10, 6))  # set the figure size
plt.scatter(x, y, alpha=0.3)  # plot the data
plt.plot(x, regression.predict(x), color='red', linewidth=4)  # plot the regression line
plt.title('Film Cost vs Global Revenue')  # set the title
plt.xlabel('Production Budget $')  # set the x label
plt.ylabel('Worldwide Gross $')  # set the y label
plt.ylim(0, 3000000000)  # set the y limit
plt.xlim(0, 450000000)  # set the x limit
print(plt.show())  # show the plot

print(regression.score(x, y))  # get the score
