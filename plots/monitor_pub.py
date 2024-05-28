import pandas as pd
import matplotlib.pyplot as plt
import csv

# Load the CSV file into a pandas DataFrame
file_path='/home/nadine_k/Documents/ZMQ/results/results-25-april/testzmq-gse-ipc-scale/resources-pub.csv'
timestamps=[]
cpu_values= []
memory_values=[]
network_values=[]
with open(file_path, 'r') as file:
    # Read the content of the file
     next(file)

     for line in file:
        # Remove leading/trailing whitespace and split the line by semicolons
        values = line.strip().split(';')

        # Extract the timestamp value and remove the ",sub1" part
        timestamp_with_sub1 = values[0].strip()
        timestamp_without_sub1 = timestamp_with_sub1.split(',')[0].strip()
        timestamp = timestamp_without_sub1.strip().split(' ')[1]
        timestamps.append(timestamp)

        # Extract the CPU value (without %) and append it to the list
        cpu_value_with_percentage = values[1].strip()
        cpu_value_without_percentage = float(cpu_value_with_percentage[:-1])  # Remove the last character (%)
        cpu_values.append(cpu_value_without_percentage)     


        # Extract the memory value before "/"
        memory_value = values[2].strip().split('/')[0].strip()
        memory_values.append(float(memory_value[:-4]))    
            
        network_value = values[3].strip().split('/')[1].strip()
        if "GB" in network_value:  # Check if the value is in GB
            network_value = float(network_value[:-2]) * 1000  # Multiply by 1000
        else:
            # network_value = float(network_value[:-2])  
            # Remove the last 2 characters (MB / B) and convert to float
            network_value=0
        network_values.append(network_value)
      
# Plotting
fig, axes = plt.subplots(3, 1, figsize=(10, 10))

# Plot CPU values
axes[0].plot(timestamps, cpu_values, color='blue')
axes[0].set_title('CPU Values')
axes[0].set_xlabel('Timestamp')
axes[0].set_ylabel('CPU (%)')
axes[0].tick_params(axis='x', rotation=45)  # Rotate x-axis labels
axes[0].tick_params(axis='both', labelsize=8)  # Increase font size
axes[0].set_xticks(timestamps[::10])  # Set x-axis ticks to every 10th time value

# Plot Memory values
axes[1].plot(timestamps, memory_values, color='green')
axes[1].set_title('Memory Values')
axes[1].set_xlabel('Timestamp')
axes[1].set_ylabel('Memory (MiB)')
axes[1].tick_params(axis='x', rotation=45)  # Rotate x-axis labels
axes[1].tick_params(axis='both', labelsize=8)  # Increase font size
axes[1].set_xticks(timestamps[::10])  # Set x-axis ticks to every 10th time value

# Plot Data values
axes[2].plot(timestamps, network_values,  color='red')
axes[2].set_title('Network Values')
axes[2].set_xlabel('Timestamp')
axes[2].set_ylabel('Data (MB)')
axes[2].tick_params(axis='x', rotation=45)  # Rotate x-axis labels
axes[2].tick_params(axis='both', labelsize=8)  # Increase font size
axes[2].set_xticks(timestamps[::10])  # Set x-axis ticks to every 10th time value


# Set common x label
axes[-1].set_xlabel('Time')

# Figure title
plt.suptitle('TestZMQ-gse-ipc-scale Publisher Resources', fontsize=16)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()