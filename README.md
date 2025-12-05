# matplotlib-project
Python script using matplot library
 Data Visualization Project

This project is part of my Python & Data Analysis learning plan.  
It covers beginner–friendly data loading, cleaning, and visualization using **Pandas** and **Matplotlib**.

The goal of this project is to understand how to work with CSV files and build simple charts based on business-related datasets.

---

## **📁 Project Files**

| File Name | Description |
|----------|-------------|
| `sales_data.csv` | Sample dataset used for analysis |
| `matplotlib_project.py` | Python script that generates all charts |
| `line_sales_trend.png` | Saved output chart (optional) |
| `bar_profit.png` | Saved output chart (optional) |
| `scatter_sales_customers.png` | Saved scatter plot |
| `pie_sales_contribution.png` | Saved pie chart |
| `hist_profit_distribution.png` | Saved histogram |
| `README.md` | Documentation for the project |

---

## **📊 Visualizations Included**

The script generates the following charts:

1. **Line Chart** – Monthly sales trend  
2. **Bar Chart** – Monthly profit  
3. **Scatter Plot** – Customers vs Sales  
4. **Pie Chart** – Month-wise contribution to total sales  
5. **Histogram** – Profit distribution  

Each chart is saved as a PNG file using:

```python
plt.savefig("chart_name.png")
