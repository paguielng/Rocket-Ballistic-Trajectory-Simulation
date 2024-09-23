import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # gravitational acceleration in m/s^2

# Initial conditions
initial_velocity = 250  # initial velocity in m/s
launch_angle = 40  # launch angle in degrees
launch_angle_rad = np.deg2rad(launch_angle)  # convert launch angle to radians

# Time values
time_step = 0.01
total_time = 2 * initial_velocity * np.sin(launch_angle_rad) / g
times = np.arange(0, total_time, time_step)

# Calculate x and y positions
x_positions = initial_velocity * np.cos(launch_angle_rad) * times
y_positions = initial_velocity * np.sin(launch_angle_rad) * times - 0.5 * g * times**2

# Plot the trajectory
plt.plot(x_positions, y_positions)
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.title('Ballistic Trajectory of a Rocket')
plt.grid()
plt.show()
