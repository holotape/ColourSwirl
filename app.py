import matplotlib.pyplot as plt
import numpy as np

def create_fading_swirl(ax, start_deg, end_deg, color):
    # Generate theta values
    theta = np.linspace(np.radians(start_deg), np.radians(end_deg), 300)
    
    # Calculate radius to create a fading swirl effect
    r = np.linspace(0, 0.4, len(theta))
    
    # Convert polar to cartesian coordinates
    x = r * np.cos(theta) + 0.5
    y = r * np.sin(theta) + 0.5
    
    # Plot the swirl
    ax.plot(x, y, color=color, linewidth=1)

# Create a figure and a single subplot
fig, ax = plt.subplots()

create_fading_swirl(ax, 0, 120, 'red')
create_fading_swirl(ax, 120, 240, 'blue')
create_fading_swirl(ax, 240, 360, 'green')

# Set aspect of the plot to be equal and remove axes
ax.set_aspect('equal', adjustable='box')
plt.axis('off')

# Drawing a black circle around the outer extremes of the spiral
circle = plt.Circle((0.5, 0.5), 0.4, color='black', fill=False, linewidth=1.0)
ax.add_artist(circle)

# Set limits for x and y axes
ax.set_xlim(0.1, 0.9)
ax.set_ylim(0.1, 0.9)

# Save the plot as a PNG file
plt.savefig('swirl_pattern.png', dpi=300)

# Show the plot
plt.show()
