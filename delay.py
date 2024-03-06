import csv
import re

def extract_parameters_from_csv(csv_file,limit):
    parameters = {}
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for cell in row:
                match = re.search(r'SqNum: (\d+) t: (\d+)', cell)
                if match:
                    sq_num = int(match.group(1))
                    t_value = int(match.group(2))
                    if sq_num >= limit:
                        parameters[sq_num] = [t_value]
    return parameters

def subtract_t_values(parameters1, parameters2, output_csv_file): 
    subtracted_values = []
    for sq_num in parameters2:
            t_values1 = parameters1[sq_num]
            t_values2 = parameters2[sq_num]
            difference = sum(t_values2) - sum(t_values1)
            subtracted_values.append((sq_num, difference))
    
    with open(output_csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['SqNum', 'Difference', 'First Parameter'])
        writer.writerows(subtracted_values)

# Example usage:
csv_file1 = 'test1.csv'
csv_file2 = 'test2.csv'
output_csv_file='out.csv'

parameters2 = extract_parameters_from_csv(csv_file2,0)
SqNum0, t0 = next(iter(parameters2.items()))
parameters1 = extract_parameters_from_csv(csv_file1,SqNum0)

subtract_t_values(parameters1, parameters2, output_csv_file)