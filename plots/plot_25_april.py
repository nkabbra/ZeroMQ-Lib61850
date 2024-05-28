import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-25-april-processed/testzmq/non_outliers.csv'
x1_values, y1_values = read_values_from_csv(csv_file)

x1_values=x1_values[:4000000]
y1_values=y1_values[:4000000]


# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-25-april-processed/testzmq-gse/non_outliers.csv'
x2_values, y2_values = read_values_from_csv(csv_file)


x2_values=x2_values[:4000000]
y2_values=y2_values[:4000000]



# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april/testzmq-gse-ipc/non_outliers.csv'
x3_values, y3_values = read_values_from_csv(csv_file)


x3_values=x3_values[:4000000]
y3_values=y3_values[:4000000]


# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april/testgse/non_outliers.csv'
x4_values, y4_values = read_values_from_csv(csv_file)

x4_values=x4_values[:4000000]
y4_values=y4_values[:4000000]





# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april/testzmq-gse-scale/non_outliers.csv'
x5_values, y5_values = read_values_from_csv(csv_file)

x5_values=x5_values[:4000000]
y5_values=y5_values[:4000000]


# # # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april/testzmq-scale/non_outliers7.csv'
x6_values, y6_values = read_values_from_csv(csv_file)

x6_values=x6_values[:4000000]
y6_values=y6_values[:4000000]


# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april/testzmq-gse-scale2/non_outliers7.csv'
x7_values, y7_values = read_values_from_csv(csv_file)

x7_values=x7_values[:4000000]
y7_values=y7_values[:4000000]


# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april/testzmq-scale2/non_outliers7.csv'
x8_values, y8_values = read_values_from_csv(csv_file)

x8_values=x8_values[:4000000]
y8_values=y8_values[:4000000]


# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april/testgse-scale/non_outliers.csv'
x9_values, y9_values = read_values_from_csv(csv_file)

x9_values=x9_values[:4000000]
y9_values=y9_values[:4000000]




# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-25-april-processed/testipc-scale/non_outliers.csv'
x10_values, y10_values = read_values_from_csv(csv_file)

x10_values=x10_values[:4000000]
y10_values=y10_values[:4000000]



# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-25-april-processed/testzmq-gse-ipc-scale/non_outliers.csv'
x11_values, y11_values = read_values_from_csv(csv_file)

x11_values=x11_values[:4000000]
y11_values=y11_values[:4000000]


# # Example usage:
csv_file = '/home/nadine_k/Documents/ZMQ/results/results-15-april/testzmq-ipc/non_outliers1.csv'
x12_values, y12_values = read_values_from_csv(csv_file)

x12_values=x12_values[:4000000]
y12_values=y12_values[:4000000]


# Plot the data

# Set x-axis ticks to increment by 100


# Plot histogram of y values

# plot_normalized_histogram(y1_values[0:900000],'d1')
# plot_normalized_histogram(y2_values[0:900000],'d2')
# plot_normalized_histogram(y3_values [0:900000],'d3')

##############################


smoothed_y1 = pd.Series(y1_values).rolling(window=10).mean()
smoothed_y2= pd.Series(y2_values).rolling(window=10).mean()
smoothed_y3 = pd.Series(y3_values).rolling(window=10).mean()
smoothed_y4= pd.Series(y4_values).rolling(window=10).mean()
smoothed_y12= pd.Series(y12_values).rolling(window=10).mean()

colors = ['#6495ED', '#3CB371', '#FF6347', '#DAA520', '#F08080']


################################

plt.figure(figsize=(10, 6)) 

# Calculate the average of the original y values
average_y2 = pd.Series(y2_values).mean()
average_y3 = pd.Series(y3_values).mean()

plt.plot(x2_values[::9000], smoothed_y2[::9000],  color= colors[0], label='dzmq-gse-tcp')
plt.plot(x3_values[::9000], smoothed_y3[::9000], color=colors[1], label='dzmq-gse-ipc')


plt.axhline(y=average_y2,  color=colors[0], linestyle='--')
plt.axhline(y=average_y3, color=colors[1], linestyle='--')

plt.title('testZMQ-gse tcp vs ipc')
plt.xlabel('SqNum')
plt.ylabel('Latency in µs')
plt.legend()


###############################

plt.figure(figsize=(10, 6)) 

smoothed_y12 = pd.Series(y12_values).rolling(window=10).mean()
average_y12 = pd.Series(y12_values).mean()
average_y1 = pd.Series(y1_values).mean()
average_y4 = pd.Series(y4_values).mean()

plt.plot(x12_values[::9000], smoothed_y12[::9000], color=colors[2],label='dzmq-ipc')
plt.plot(x1_values[::9000], smoothed_y1[::9000],color=colors[3],label='dzmq-tcp')
plt.plot(x4_values[::9000], smoothed_y4[::9000], color=colors[4], label='dgse')
plt.axhline(y=average_y12,  color=colors[2], linestyle='--')
plt.axhline(y=average_y1, color=colors[3], linestyle='--')
plt.axhline(y=average_y4, color=colors[4], linestyle='--')

plt.title('testZMQ / GSE')
plt.xlabel('SqNum')
plt.ylabel('Latency in µs')
plt.legend()


##############################

plt.figure(figsize=(10, 6)) 
average_y10 = pd.Series(y10_values).mean()
average_y6 = pd.Series(y6_values).mean()
average_y9 = pd.Series(y9_values).mean()

smoothed_y10 = pd.Series(y10_values).rolling(window=10).mean()
smoothed_y6= pd.Series(y6_values).rolling(window=10).mean()
smoothed_y9 = pd.Series(y9_values).rolling(window=10).mean()

plt.plot(x10_values[::9000], smoothed_y10[::9000], color=colors[2], label='dzmq-ipc scale-sub')
plt.plot(x6_values[::9000], smoothed_y6[::9000], color=colors[3], label='dzmq-tcp scale-sub')
plt.plot(x9_values[::9000], smoothed_y9[::9000], color=colors[4],label='dgse scale-sub')

plt.axhline(y=average_y10,  color=colors[2], linestyle='--')
plt.axhline(y=average_y6, color=colors[3], linestyle='--')
plt.axhline(y=average_y9, color=colors[4], linestyle='--')

plt.title('testZMQ-scaled-sub')
plt.xlabel('SqNum')
plt.ylabel('Latency in µs')
plt.legend()

############################

plt.figure(figsize=(10, 6)) 

smoothed_y11 = pd.Series(y11_values).rolling(window=10).mean()
smoothed_y5= pd.Series(y5_values).rolling(window=10).mean()
average_y11 = pd.Series(y11_values).mean()
average_y5 = pd.Series(y5_values).mean()
average_y9 = pd.Series(y9_values).mean()

plt.plot(x11_values[::9000], smoothed_y11[::9000], color=colors[1],label='dzmq-gse-ipc scale-sub')
plt.plot(x5_values[::9000], smoothed_y5[::9000], color=colors[0],label='dzmq-gse-tcp scale-sub')
plt.plot(x9_values[::9000], smoothed_y9[::9000], color=colors[4], label='dgse scale-sub')

plt.axhline(y=average_y11,  color=colors[1], linestyle='--')
plt.axhline(y=average_y5, color=colors[0], linestyle='--')
plt.axhline(y=average_y9,color=colors[4], linestyle='--')

plt.title('testZMQ-gse-scaled-sub')
plt.xlabel('SqNum')
plt.ylabel('Latency in µs')
plt.legend()



plt.grid(True)
plt.show()