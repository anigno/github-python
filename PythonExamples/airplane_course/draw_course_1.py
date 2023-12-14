import matplotlib.pyplot as plt
import numpy as np

def calculate_next_position(current_x, current_y, azimuth_degrees, speed, time):
    azimuth_radians = np.radians(azimuth_degrees)
    next_x = current_x + speed * time * np.cos(azimuth_radians)
    next_y = current_y + speed * time * np.sin(azimuth_radians)
    return next_x, next_y

def draw_airplane_course(start_x, start_y, initial_azimuth, speed, total_time, time_interval):
    x_values = [start_x]
    y_values = [start_y]

    current_x, current_y = start_x, start_y
    current_azimuth = initial_azimuth

    for _ in np.arange(0, total_time, time_interval):
        current_x, current_y = calculate_next_position(current_x, current_y, current_azimuth, speed, time_interval)
        x_values.append(current_x)
        y_values.append(current_y)

    plt.plot(x_values, y_values, label="Airplane Course", marker='o')
    plt.scatter([start_x], [start_y], color='red', label="Start Point", marker='o')
    plt.scatter([current_x], [current_y], color='green', label="End Point", marker='o')

    plt.title("Airplane Course")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
start_x = 0
start_y = 0
initial_azimuth = 45  # Angle in degrees
speed = 10  # Speed in units per time
total_time = 10  # Total time for simulation
time_interval = 1  # Time interval for each step

draw_airplane_course(start_x, start_y, initial_azimuth, speed, total_time, time_interval)
