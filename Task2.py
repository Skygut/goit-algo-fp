import matplotlib.pyplot as plt
import numpy as np


def draw_square(ax, origin, length, angle):
    """
    Draw a square and return the top right corner and top left corner coordinates.
    """
    # Define the square coordinates based on origin and angle
    square_coords = [
        origin,
        [
            origin[0] + length * np.cos(np.radians(angle)),
            origin[1] + length * np.sin(np.radians(angle)),
        ],
        [
            origin[0]
            + length * np.cos(np.radians(angle))
            - length * np.sin(np.radians(angle)),
            origin[1]
            + length * np.sin(np.radians(angle))
            + length * np.cos(np.radians(angle)),
        ],
        [
            origin[0] - length * np.sin(np.radians(angle)),
            origin[1] + length * np.cos(np.radians(angle)),
        ],
    ]

    # Close the square path
    square_coords.append(square_coords[0])
    square_coords = np.array(square_coords)

    # Draw the square
    ax.plot(square_coords[:, 0], square_coords[:, 1], "black")

    # Return the top corners of the square
    return square_coords[2], square_coords[3]


def draw_pythagoras_tree(ax, origin, length, angle, depth):
    """
    Recursively draw the Pythagoras tree.
    """
    if depth == 0:
        return

    # Draw the base square and get the top corners
    top_right, top_left = draw_square(ax, origin, length, angle)

    # Calculate new squares' sizes using Pythagoras theorem
    new_length = length / np.sqrt(2)

    # Draw the right and left squares on top of the base square
    draw_pythagoras_tree(ax, top_right, new_length, angle + 45, depth - 1)
    draw_pythagoras_tree(ax, top_left, new_length, angle - 45, depth - 1)


# Parameters
initial_length = 1  # Initial square side length
initial_depth = 10  # Depth of recursion

# Create a figure
fig, ax = plt.subplots()
ax.set_aspect("equal", adjustable="box")

# Hide axes
ax.axis("off")

# Draw the Pythagoras tree
draw_pythagoras_tree(ax, [0, 0], initial_length, 0, initial_depth)

# Show the plot
plt.show()
