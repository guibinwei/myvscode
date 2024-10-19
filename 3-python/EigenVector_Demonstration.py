import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Define the matrix A
A = np.array([[2, 1],
              [1, 2]])

# Calculate eigenvectors and eigenvalues
eigenvalues, eigenvectors = np.linalg.eig(A)

# Create a grid of points
x = np.arange(-2, 2.1, 0.5)
y = np.arange(-2, 2.1, 0.5)
X, Y = np.meshgrid(x, y)

# Transform the grid
XY = np.array([X.flatten(), Y.flatten()])
XY_transformed = A @ XY
X_transformed = XY_transformed[0].reshape(X.shape)
Y_transformed = XY_transformed[1].reshape(Y.shape)

# Create the plot
plt.figure(figsize=(10, 10))

# Plot original grid
plt.plot(X.flatten(), Y.flatten(), 'k.', markersize=5)

# Plot transformed grid
plt.plot(X_transformed.flatten(), Y_transformed.flatten(), 'r.', markersize=5)

# Plot eigenvectors
for eigenvector in eigenvectors.T:
    plt.arrow(0, 0, eigenvector[0], eigenvector[1], color='g', width=0.02, head_width=0.1)

# Plot matrix column vectors
for column in A.T:
    plt.arrow(0, 0, column[0], column[1], color='b', width=0.02, head_width=0.1)

# Set labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Matrix Transformation and Eigenvectors')

# Set axis limits
plt.xlim(-6, 6)
plt.ylim(-6, 6)

# Create custom legend handles
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Original Grid', markerfacecolor='k', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Transformed Grid', markerfacecolor='r', markersize=10),
    Line2D([0], [0], color='g', lw=2, label='Eigenvectors'),
    Line2D([0], [0], color='b', lw=2, label='Matrix Columns')
]

# Add legend with custom handles
plt.legend(handles=legend_elements, loc='upper left')

# Show grid
plt.grid(True)

# Ensure equal aspect ratio
plt.axis('equal')

# Show the plot
plt.show()