import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# 1. Line Chart - Sales growth
plt.figure()
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("line_sales_trend.png")   # Save chart
plt.show()

# 2. Bar Chart - Profit
plt.figure()
plt.bar(df["Month"], df["Profit"])
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.savefig("bar_profit.png")   # Save chart
plt.show()

# 3. Scatter Chart - Customers vs Sales
plt.figure()
plt.scatter(df["Customers"], df["Sales"])
plt.title("Customers vs Sales")
plt.xlabel("Customers")
plt.ylabel("Sales")
plt.savefig("scatter_sales_customers.png")   # Save chart
plt.show()

# 4. Pie Chart - Total Sales Contribution
plt.figure()
plt.pie(df["Sales"], labels=df["Month"], autopct="%1.1f%%")
plt.title("Sales Contribution by Month")
plt.savefig("pie_sales_contribution.png")   # Save chart
plt.show()

# 5. Histogram - Profit Distribution
plt.figure()
plt.hist(df["Profit"])
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.savefig("hist_profit_distribution.png")   # Save chart
plt.show()
