
import matplotlib.pyplot as plt
import numpy as np

#define the points 5
center_x = float(input("Enter the x-coordinate of the center: "))
center_y = float(input("Enter the y-coordinate of the center: "))
radius = float(input("Enter the radius of the circle: "))

theta = np.linspace(0, 2*np.pi, 100)


# Calculate the x and y coordinates of the points on the circle

x = center_x+radius * np.cos(theta)
y = center_y+radius * np.sin(theta)

# Create a new figure and axis
fig, ax = plt.subplots()

# Plot the circle using the x and y coordinates
ax.plot(x, y)

# Set the aspect ratio to be equal, so the circle is not distorted
ax.set_aspect('equal', adjustable='box')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Circle using Matplotlib')

# Display the plot
plt.show()
