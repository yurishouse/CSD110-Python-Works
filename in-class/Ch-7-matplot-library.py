import matplotlib.pyplot as plt

x_coords = [0, 1, 2, 3, 4]

y_coords = [0, 3, 1, 5, 2]

# build the line plot
plt.bar(x_coords, y_coords)

# Add a title
plt.title("This is a graph")

# add a label to x/y
plt.xlabel("This is the x")
plt.ylabel("This is the y")

# gives the ticks a different name
plt.xticks([0, 1, 2, 3, 4], ["2016", "2017", "2018", "2019", "2020"])
plt.yticks([0, 1, 2, 3, 4], ["$0m", "$1m", "$2m", "$3m", "$4m"])
# Show the grid
plt.grid(True)

# Show the graph
plt.show()
