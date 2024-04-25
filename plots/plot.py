import csv
import numpy as np
import matplotlib.pyplot as plt

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
    plt.title('Normalized Value Distribution (Second Column)')
    plt.legend()
    plt.xlabel('Normalized Value')
    plt.ylabel('Frequency')
    

# Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-21-march/testzmq2/non_outliers.csv'
x1_values, y1_values = read_values_from_csv(csv_file)

# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-21-march/testzmq-gse3/non_outliers.csv'
x2_values, y2_values = read_values_from_csv(csv_file)

# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april-processed/testzmq-gse-ipc/non_outliers.csv'
x3_values, y3_values = read_values_from_csv(csv_file)

# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april-processed/testgse/non_outliers.csv'
x4_values, y4_values = read_values_from_csv(csv_file)

x4_values=x4_values[:4000000]
y4_values=y4_values[:4000000]





# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april-processed/testzmq-gse-scale/non_outliers7.csv'
x5_values, y5_values = read_values_from_csv(csv_file)
x5_values=x5_values[:4000000]
y5_values=y5_values[:4000000]



# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april-processed/testzmq-scale/non_outliers7.csv'
x6_values, y6_values = read_values_from_csv(csv_file)

x6_values=x6_values[:4000000]
y6_values=y6_values[:4000000]



# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april-processed/testzmq-gse-scale2/non_outliers7.csv'
x7_values, y7_values = read_values_from_csv(csv_file)
x7_values=x7_values[:4000000]
y7_values=y7_values[:4000000]



# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april-processed/testzmq-scale2/non_outliers7.csv'
x8_values, y8_values = read_values_from_csv(csv_file)

x8_values=x8_values[:4000000]
y8_values=y8_values[:4000000]

# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april-processed/testgse-scale/non_outliers.csv'
x9_values, y9_values = read_values_from_csv(csv_file)

x9_values=x9_values[:4000000]
y9_values=y9_values[:4000000]






# Plot the data

# Set x-axis ticks to increment by 100


# Plot histogram of y values

# plot_normalized_histogram(y1_values[0:1000000],'d1')
# plot_normalized_histogram(y2_values[0:1000000],'d2')
# plot_normalized_histogram(y3_values [0:1000000],'d3')


plt.figure(figsize=(10, 6)) 
plt.plot(x1_values[::10000], y1_values[::10000],label='dzmq')
plt.plot(x2_values[::10000], y2_values[::10000],label='dzmq-gse-tcp')
plt.plot(x4_values[::10000], y4_values[::10000],label='dgse')

plt.xlabel('SqNum')
plt.ylabel('Latency in µs')
plt.legend()


plt.figure(figsize=(10, 6)) 
plt.plot(x2_values[::10000], y2_values[::10000],label='dzmq-gse-tcp')
plt.plot(x3_values[::10000], y3_values[::10000],label='dzmq-gse-ipc')
plt.title('testZMQ-gse tcp vs ipc')
plt.xlabel('SqNum')
plt.ylabel('Latency in µs')
plt.legend()


plt.figure(figsize=(10, 6)) 
plt.plot(x1_values[::9000], y1_values[::9000],label='dzmq')
plt.plot(x6_values[::9000], y6_values[::9000],label='dzmq scale')
# plt.plot(x8_values[::10000], y8_values[::10000],label='dzmq scale 2')
plt.plot(x4_values[::10000], y4_values[::10000],label='dgse')
plt.plot(x9_values[::10000], y9_values[::10000],label='dgse scale')

plt.title('testZMQ-scaled')
plt.xlabel('SqNum')
plt.ylabel('Latency in µs')
plt.legend()


plt.figure(figsize=(10, 6)) 
plt.plot(x2_values[::10000], y2_values[::10000],label='dzmq-gse-tcp')
plt.plot(x4_values[::10000], y4_values[::10000],label='dgse')
plt.plot(x5_values[::10000], y5_values[::10000],label='dzmq-gse-tcp scale')
# plt.plot(x7_values[::10000], y7_values[::10000],label='dzmq-gse-tcp scale2')
plt.plot(x9_values[::10000], y9_values[::10000],label='dgse scale')


plt.title('testZMQ-gse-scaled')
plt.xlabel('SqNum')
plt.ylabel('Latency in µs')
plt.legend()


plt.grid(True)
plt.show()