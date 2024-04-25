import csv
import re

def filter_and_save(input_file, output_file, non_outliers_file, limit):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile, open(non_outliers_file, 'w', newline='') as non_outliers_file:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        non_outliers_writer = csv.writer(non_outliers_file)
        for row in reader:
            try:
                value = float(row[1])  # Assuming the second column contains numerical values
                if value >= limit:
                    writer.writerow(row)
                else:
                    non_outliers_writer.writerow(row)
            except ValueError:
                pass  # Ignore rows where the second column is not a valid number

def count_elements(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # Exclude the header row if it exists
        header = next(reader, None)
        count = sum(1 for row in reader)
    return count

# Example usage:
input_file = 'delay15.csv'
output_file = 'outliers15.csv'
non_outliers_file = 'non_outliers15.csv'
limit = 3300  # Set your desired limit here

filter_and_save(input_file, output_file, non_outliers_file, limit)

per=( count_elements(output_file)/ count_elements(input_file) ) * 100
print("percentage outliers is:")
print(per)
