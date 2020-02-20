import matplotlib.pyplot as plt

data = [12, 34, 55, 64]
name = ["pig", "bird", "cat", "dog"]
plt.pie(data, labels=name)

plt.title("The % of pets")


plt.show()