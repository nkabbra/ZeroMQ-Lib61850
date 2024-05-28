import csv
import re

def extract_parameters_from_csv_pub(csv_file,limit):
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
            # Convert parameters dictionary to a list of lists for CSV writing
    data = [['SqNum', 't_values']]  # Header
    for sq_num, t_values in sorted(parameters.items()):
        data.append([sq_num, ','.join(map(str, t_values))])
    
    return data

def extract_parameters_from_csv_sub(csv_file):
    parameters = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for cell in row:
                match = re.search(r'value is (\S+) t: (\d+)', cell)
                if match:
                    sq_num = (match.group(1))
                    t_value = int(match.group(2))
                    if sq_num == 'trueee':
                        parameters.append([sq_num, t_value])


    return parameters

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


# Example usage:
pub = '/home/nadine_k/Documents/ZMQ/results/results_case_study/testzmq-tcp10/testpub1/log.csv'
sub = '/home/nadine_k/Documents/ZMQ/results/results_case_study/testzmq-tcp10/log.csv'
gate = '/home/nadine_k/Documents/ZMQ/results/results_case_study/testzmq-tcp10/testtg/log.csv'

output_csv_file1='pub.csv'
output_csv_file2='sub.csv'
output_csv_file3='tg.csv'

# parameters_sub = extract_parameters_from_csv(sub,0)

# SqNum0, t0 = next(iter(parameters_sub.items()))
# parameters_pub = extract_parameters_from_csv_pub(pub,0)
# parameters_sub = extract_parameters_from_csv_sub(sub)
parameters_tg = extract_parameters_from_csv_sub(gate)

# save_to_csv(parameters_pub,output_csv_file1)
# save_to_csv(parameters_sub,output_csv_file2)
save_to_csv(parameters_tg,output_csv_file3)
