import matplotlib.pyplot as plt 

#Life expectancy of different countries
life_exp = [55.61, 52.71, 45.25, 76.69, 78.38, 64.49, 60.77, 69.09, 52.09, 75.24, 
            60.11, 69.74, 66.63, 61.16, 51.02, 62.36, 66.95, 48.83, 51.47, 77.59, 
            55.58, 76.93, 57.19, 70.2, 45.1, 52.91, 51.93, 46.27, 65.96, 59.76]

# ---> 1
# Generate a histogram 1
plt.hist(life_exp, bins=5)

# Display the histogram
plt.show()
# Clean up the histogram
plt.clf()

# ---> 2
# Generate histogram 2
plt.hist(life_exp, bins=20)

# Display the histogram
plt.show()
# Clean up histogram
plt.clf()