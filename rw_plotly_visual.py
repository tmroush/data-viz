import plotly.express as px

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
fig = px.scatter(rw.x_values, rw.y_values)
fig.show()
