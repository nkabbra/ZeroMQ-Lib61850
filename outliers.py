import csv

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

# Example usage:
input_file = 'test1.csv'
output_file = 'outliers.csv'
non_outliers_file = 'non_outliers.csv'
limit = 10  # Set your desired limit here

filter_and_save(input_file, output_file, non_outliers_file, limit)
