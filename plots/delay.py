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
            if sq_num in parameters1:
                t_values1 = parameters1[sq_num]
                t_values2 = parameters2[sq_num]
                difference = sum(t_values2) - sum(t_values1)
                subtracted_values.append((sq_num, difference))
            else:
                    print(sq_num)
    
    with open(output_csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['SqNum', 'Difference'])
        writer.writerows(subtracted_values)

# Example usage:
pub = '/home/nadine_k/Documents/ZMQ/results/results-15-april/testzmq-scale2/testpub1/log.csv'
sub = '/home/nadine_k/Documents/ZMQ/results/results-15-april/testzmq-scale2/testsub15/log.csv'
gate = 'results/testzmq-gse-sub-d1-new/testgate1/log.csv'

output_csv_file='delay15.csv'

parameters_sub = extract_parameters_from_csv(sub,0)

SqNum0, t0 = next(iter(parameters_sub.items()))
parameters_pub = extract_parameters_from_csv(pub,SqNum0)
print(len(parameters_sub))
print(len(parameters_pub))
subtract_t_values(parameters_pub, parameters_sub, output_csv_file)
