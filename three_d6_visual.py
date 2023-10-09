from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create 1 d6 and 1 d10.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls and store results in a list.
results = [die_1.roll()+die_2.roll()+die_3.roll() for roll_num in range(50000)]

# Figure out how many of each number (1-6) was rolled:

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result+1)]

# Visualize the results:
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a three D6 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6x3.html')
