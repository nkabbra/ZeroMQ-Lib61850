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
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-20-march/testzmq-gse-ipc/delay.csv'
x1_values, y1_values = read_values_from_csv(csv_file)

# # Example usage:
# csv_file = 'delay2.csv'
# x2_values, y2_values = read_values_from_csv(csv_file)

# # Example usage:
# csv_file = 'delay3.csv'
# x3_values, y3_values = read_values_from_csv(csv_file)

# # Example usage:
# csv_file = 'delay4.csv'
# x4_values, y4_values = read_values_from_csv(csv_file)

# # Example usage:
# csv_file = 'delay5.csv'
# x5_values, y5_values = read_values_from_csv(csv_file)

# # Example usage:
# csv_file = 'delay6.csv'
# x6_values, y6_values = read_values_from_csv(csv_file)

# # Example usage:
# csv_file = 'delay7.csv'
#x7_values, y7_values = read_values_from_csv(csv_file)


plt.figure()
# Plot histogram of y values

plot_normalized_histogram(y1_values,'d0')
#plot_normalized_histogram(y2_values[0:1000000],'d5-sub')
#plot_normalized_histogram(y5_values [0:1000000],'d5-gate')


plt.figure()
plt.plot(x1_values, y1_values,label='d1')
# plt.plot(x2_values, y2_values,label='d2')

# plt.plot(x3_values, y3_values,label='d3')

# plt.plot(x4_values, y4_values,label='d4')

# plt.plot(x5_values, y5_values,label='d5')

# plt.plot(x6_values, y6_values,label='d6')
#plt.plot(x7_values, y7_values,label='d7')


#plt.plot(x2_values[20000:100000], y2_values[20000:100000],label='d5-sub')
#plt.plot(x5_values[20000:100000], y5_values[20000:100000],label='d5-gate')

plt.title('Y as a function of X')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()


plt.grid(True)
plt.show()