import matplotlib.pyplot as plt
import numpy as np

def create_fading_swirl(ax, start_deg, end_deg, color):
    theta = np.linspace(np.radians(start_deg), np.radians(end_deg), 300)
    
    r = np.linspace(0, 0.4, len(theta))
    
    x = r * np.cos(theta) + 0.5
    y = r * np.sin(theta) + 0.5
    
    ax.plot(x, y, color=color, linewidth=1.0)

def create_dense_fading_swirl(ax, start_deg, end_deg, color, step=1):
    for offset in range(0, 120, step):
        create_fading_swirl(ax, start_deg + offset, end_deg + offset, color)

fig, ax = plt.subplots()

create_dense_fading_swirl(ax, 92, 212, 'green')
create_dense_fading_swirl(ax, 212, 332, 'red')
create_dense_fading_swirl(ax, 332, 452, 'blue')

# set aspect of the plot to be equal and remove axes
ax.set_aspect('equal', adjustable='box')
plt.axis('off')

# black circle around the outer extremes of the spiral
circle = plt.Circle((0.5, 0.5), 0.401, color='black', fill=False, linewidth=1.0, zorder=3)
ax.add_artist(circle)

# set limits for x and y axes
ax.set_xlim(0.01, 0.99)
ax.set_ylim(0.01, 0.99)

# Save the plot as a PNG file
plt.savefig('swirl_pattern.png', dpi=600)
plt.savefig('swirl_pattern.svg', format='svg')


# Show the plot
plt.show()
