import matplotlib.pyplot as plt

# Students
students = [17, 5, 12, 9, 18, 11, 6, 23, 5, 7, 9, 20, 18, 17, 23, 12, 24, 23, 22, 18, 11, 7, 24, 16, 7, 24, 12, 12, 5, 21]
# Ranks
ranks = [44, 27, 16, 28, 8, 4, 28, 22, 45, 44, 39, 16, 43, 34, 20, 16, 6, 12, 15, 45, 45, 13, 7, 22, 30, 39, 48, 11, 37, 15]

population = [241, 52, 415, 88, 326, 389, 219, 159, 299, 122, 51, 347, 445, 344, 483, 31, 428, 121, 391, 175, 168, 484, 414, 405, 264, 23, 297, 53, 92, 233]

# Dictionary for reference --> To choose color of dot
continent_dictionary = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
col = ["black", "red", "yellow", "blue", "red", "blue", "black", "green", 
        "black", "blue", "black", "blue", "green", "black", "red", "green", "yellow", 
        "black", "yellow", "yellow", "blue", "green", "black", "green", "yellow", "blue", "red", "yellow", "red", "green"]

# Generate a scatter plot ( x axis -> students, y axis -> ranks, s => size of dot, c => color of dot )
plt.scatter(students, ranks, s = population, c = col)

# To put the x-axis on a logarithmic scale
# plt.xscale('log')

# Display the plot
plt.show()

#Take-away : Scatter plot is useful when there's a need to assess correlation between two variables