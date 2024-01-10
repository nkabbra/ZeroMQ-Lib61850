import re

# Specify the file path
file_path = 'logs.txt'
output_file_path = 'differences.txt'


# Define the regular expression pattern for elapsed time
pattern_elapsed_time = r'elapsed time-g: (\d+) usec'

# Open the file and read its content
with open(file_path, 'r') as file:
    file_content = file.read()

# Use re.findall to find all matches of the pattern in the content
matches_elapsed_time = re.findall(pattern_elapsed_time, file_content)

elapsed_times = [int(match) for match in matches_elapsed_time]
differences = [elapsed_times[i + 1] - elapsed_times[i] for i in range(len(elapsed_times) - 1)]

# Write differences to the output file
with open(output_file_path, 'w') as output_file:
    for diff in differences:
        output_file.write(f'Difference: {diff} usec\n')

print(f'Differences saved to {output_file_path}')