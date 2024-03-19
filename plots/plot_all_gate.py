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



def plot_normalized_histogram(values,l):
    # Normalize the values
    values = np.array(values)
    # Plot the histogram
    plt.hist(values, bins=10, alpha=0.7, label= l)
    plt.title('Normalized Value Distribution Delay Sub')
    plt.legend()
    plt.xlabel('Normalized Value')
    plt.ylabel('Frequency')
    



# Example usage:
csv_file = 'results/testzmq-gse-d0-new/delay.csv'
x0_values, y0_values = read_values_from_csv(csv_file)

# Example usage:
csv_file = 'results/testzmq-gse-d1/delay.csv'

x1_values, y1_values = read_values_from_csv(csv_file)


# Example usage:
csv_file = 'results/testzmq-gse-d2/delay.csv'
x2_values, y2_values = read_values_from_csv(csv_file)

# Example usage:
csv_file = 'results/testzmq-gse-d5/delay.csv'

x5_values, y5_values = read_values_from_csv(csv_file)


#Example usage:
csv_file = 'results/testzmq-gse-d10/delay.csv'
x10_values, y10_values = read_values_from_csv(csv_file)




# #Example usage:
# csv_file = 'results/testsub-d100/delay.csv'
# x100_values, y100_values = read_values_from_csv(csv_file)

plt.figure()
# Plot histogram of y values
#plot_normalized_histogram(y0_values,'d0')
plot_normalized_histogram(y1_values,'d1')
plot_normalized_histogram(y2_values,'d2')
plot_normalized_histogram(y5_values,'d5')
plot_normalized_histogram(y10_values,'d10')

plt.figure()
plt.plot(x0_values[20000:100000], y0_values[20000:100000],label='d0')
plt.plot(x1_values[20000:100000], y1_values[20000:100000],label='d1')
plt.plot(x2_values[20000:100000], y2_values[20000:100000],label='d2')
plt.plot(x5_values[20000:100000], y5_values[20000:100000],label='d5')
plt.plot(x10_values[20000:100000], y10_values[20000:100000],label='d10')
plt.legend()
plt.title('Y as a function of X')
plt.xlabel('X')
plt.ylabel('Y')


plt.grid(True)
plt.show()