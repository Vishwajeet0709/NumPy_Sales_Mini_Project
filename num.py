import numpy as np

months = np.array(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

sales = []

print("Enter the sales (in $1000) for each month: ")

for month in months:
    value = float(input(f"{month}: "))
    sales.append(value)

sales = np.array(sales)

print("\n====Company Sales Analysis====")
print("Total Sales of the Year: ", np.sum(sales),"$")
print("Average Monthly Sales: ", np.mean(sales),"$")
print("Highest Sales Month: ", np.max(sales),"$")
print("Lowest Sales Month: ", np.min(sales),"$")

best_month = months[np.argmax(sales)]
worst_month = months[np.argmin(sales)]
print("Best Month: ", best_month)
print("Worst Month: ", worst_month)

    
above_avg = months[sales > np.mean(sales)]
below_avg = months[sales < np.mean(sales)]
print("Months with Sales Above Average:", above_avg)
print("Months with Sales Below Average:", below_avg)



    
    
    
