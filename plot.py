import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def read_values_from_csv(csv_file):
    x_values = []
    y_values = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                x = float(row[0])  # First column value
                y = float(row[1])  # Second column value
                x_values.append(x)
                y_values.append(y)
            except ValueError:
                pass  # Ignore rows where the values are not valid numbers

    return x_values, y_values



def plot_normalized_histogram(values):
    # Normalize the values
    values = np.array(values)
    # Plot the histogram
    plt.hist(values, bins=30, color='blue', alpha=0.7)
    plt.title('Normalized Value Distribution (Second Column)')
    plt.xlabel('Normalized Value')
    plt.ylabel('Frequency')
    

# Example usage:
csv_file = 'test.csv'
x_values, y_values = read_values_from_csv(csv_file)

plt.figure()
# Plot histogram of y values

plot_normalized_histogram(y_values)

plt.figure()
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.title('Y as a function of X')
plt.xlabel('X')
plt.ylabel('Y')


plt.grid(True)
plt.show()

