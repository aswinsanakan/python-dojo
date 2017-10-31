import matplotlib.pyplot as plt

# Year
year = [1950, 1956, 1978, 1984, 1990, 1994, 2000, 2006, 2011, 2017 ]
# Population
pop = [2.5, 2.9, 3.5, 4.3, 5.2, 5.9, 6.3, 6.5, 6.7, 6.9]

# Generate a line plot ( x axis -> year, y axis -> pop )
plt.plot(year, pop)

plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population Projections")
plt.yticks([0,2,4,6,8],
            ['0','2B','4B','6B','8B'])

# Display the plot
plt.show()

#Take-away : Line plot is good when there's a time scale around horizontal axis.