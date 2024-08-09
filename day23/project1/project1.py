import pandas as pd

import matplotlib.pyplot as plt


sales_data = pd.read_csv("/home/bharathibk/github/python_project/day23/project1/sales_data.csv")

# print(sales_data)

# print(sales_data.info())
# print(sales_data.head())

#data_analysis

totoal_sales_by_month = sales_data.groupby(pd.to_datetime(sales_data["Date"]).dt.to_period('M'))["Amount"].sum()

print("Total sales by Month:")
print(totoal_sales_by_month)


#data visulization

totoal_sales_by_month.plot(kind="bar")
plt.title('Total Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales Amount')
plt.show()
