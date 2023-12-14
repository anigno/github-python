import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random

# Generate random points
x = [random.uniform(-3, 3) for _ in range(10)]
y = [random.uniform(-3, 3) for _ in range(10)]
z = [random.uniform(-3, 3) for _ in range(10)]

# Create the figure and plot
fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection="3d")
ax.plot3D(x, y, z, "blue", linewidth=2)

# Set labels and title
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Line Connecting Random Points")

# Customize the plot (optional)
# ax.set_xlim(-4, 4) # Set axis limits
# ax.set_ylim(-4, 4)
# ax.set_zlim(-4, 4)
# ax.view_init(elev=15, azim=-60) # Set viewpoint

plt.show()
