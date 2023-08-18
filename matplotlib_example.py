import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and axis
plt.figure(figsize=(8, 6))
plt.title("Sine and Cosine Waves")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Plot the sine wave in blue and cosine wave in red
plt.plot(x, y1, label="Sine Wave", color="blue")
plt.plot(x, y2, label="Cosine Wave", color="red")

# Add legend
plt.legend()

# Highlight data points where sine and cosine intersect
intersection_points = np.where(np.isclose(y1, y2))
plt.scatter(x[intersection_points], y1[intersection_points], color="green", label="Intersection Points")

# Annotate the intersection points
for i in intersection_points[0]:
    plt.annotate(f'({x[i]:.2f}, {y1[i]:.2f})', (x[i], y1[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

# Customize the plot appearance
plt.grid()
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xticks(np.arange(0, 2*np.pi+0.1, np.pi/2), ['0', '$\\frac{\pi}{2}$', '$\pi$', '$\\frac{3\pi}{2}$', '$2\pi$'])

# Show the plot
plt.tight_layout()
plt.show()
