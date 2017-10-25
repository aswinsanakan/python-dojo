import matplotlib.pyplot as plt

# Year
year = [1950, 1956, 1978, 1984, 1990, 1994, 2000, 2006, 2011, 2017 ]
# Population
pop = [10, 15, 18.4, 20.3, 22, 23.6, 25, 25.4, 25.9, 26.3 ]

# Generate a line plot ( x axis -> year, y axis -> pop )
plt.plot(year, pop)

# Display the plot
plt.show()