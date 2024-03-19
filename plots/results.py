import pandas as pd

def calculate_statistics(csv_file_path):
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Extract the second column
        third_column = df.iloc[:,1]  # Assumes 0-based indexing

        # Calculate statistics
        minimum_value = third_column.min()
        maximum_value = third_column.max()
        average_value = third_column.mean()
        std_deviation = third_column.std()

        return minimum_value, maximum_value, average_value, std_deviation

    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
csv_file_path = '/home/nadine_k/Documents/ZMQ/results/delay.csv'
#csv_file_path = 'results/testzmq-gse-sub-d5/outliers.csv'

statistics = calculate_statistics(csv_file_path)

if statistics is not None:
    min_value, max_value, avg_value, std_dev = statistics
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")
    print(f"Average value: {avg_value}")
    print(f"Standard Deviation: {std_dev}")
else:
    print("Unable to calculate statistics.")