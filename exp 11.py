
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_2023 = [150, 180, 220, 250, 210, 290]
sales_2024 = [170, 195, 240, 280, 235, 310]
expenses = [100, 110, 125, 130, 120, 140]

# --- 1. Line Chart ---
plt.figure(figsize=(10, 5))

# Plotting the two line charts
plt.plot(months, sales_2023, 
         marker='o', # Add circles at data points
         linestyle='-', 
         color='blue', 
         label='Sales 2023')

plt.plot(months, sales_2024, 
         marker='s', # Add squares at data points
         linestyle='--', 
         color='red', 
         label='Sales 2024')

# Adding Labels, Title, and Legend
plt.xlabel("Month of the Year")
plt.ylabel("Revenue (in Thousands)")
plt.title("Monthly Sales Comparison (2023 vs 2024)")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# --- 2. Bar Graph ---
plt.figure(figsize=(10, 5))
bar_width = 0.35
r1 = np.arange(len(months)) # Position of the bars for sales
r2 = [x + bar_width for x in r1] # Position of the bars for expenses

# Plotting the bar graph
plt.bar(r1, sales_2024, 
        color='green', 
        width=bar_width, 
        edgecolor='grey', 
        label='Sales (2024)')

plt.bar(r2, expenses, 
        color='orange', 
        width=bar_width, 
        edgecolor='grey', 
        label='Expenses (2024)')

# Adding Labels, Title, and Legend
plt.xlabel("Month", fontweight='bold')
plt.ylabel("Amount (in Thousands)", fontweight='bold')
plt.xticks([r + bar_width/2 for r in r1], months) # Center the month labels
plt.title("Monthly Sales and Expenses (Bar Chart)")
plt.legend()
plt.show()
