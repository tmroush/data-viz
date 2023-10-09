import matplotlib.pyplot as plt

from die import Die

fig, ax = plt.subplots()

# Create 1 d6 and 1 d10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls and store results in a list.
results = [die_1.roll()+die_2.roll() for roll_num in range(50000)]

# Figure out how many of each number (1-6) was rolled. These will be our x-axis stuff
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results:
x_labels = [x for x in range(2, max_result+1)]

ax.bar(x_labels, frequencies)
ax.set_ylabel('Totals')
ax.set_title('Rolling a D6 and D10 for 50000 tries')

plt.show()

