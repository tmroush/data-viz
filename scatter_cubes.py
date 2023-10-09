import matplotlib.pyplot as plt

x_values = range(1, 6)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=100)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 6, 0, 150])

# set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
