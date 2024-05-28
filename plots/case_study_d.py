import pandas as pd
results_df = pd.DataFrame(columns=['Index', 'Value'])

for i in range(1, 11):
    # Construct the file paths
    pub_file_path = f'/home/nadine_k/Documents/ZMQ/results/results_case_study_processed/testzmq-ipc{i}/pub.csv'
    sub_file_path = f'/home/nadine_k/Documents/ZMQ/results/results_case_study_processed/testzmq-ipc{i}/tg.csv'
    
    # Read the CSV files
    csv1 = pd.read_csv(pub_file_path, header=None)
    csv2 = pd.read_csv(sub_file_path, header=None)
    
    # Ensure the second column is numeric
    csv1[1] = pd.to_numeric(csv1[1], errors='coerce')
    csv2[1] = pd.to_numeric(csv2[1], errors='coerce')
    
    # Extract the value from the second column of the first row in csv1
    value_to_subtract = csv1.iloc[1, 1]
    
    # Check if value_to_subtract is valid
    if pd.isna(value_to_subtract):
        raise ValueError(f"The value to subtract in file {pub_file_path} is not a valid number.")
    
    # Subtract this value from the second column of the first row in csv2
    result_value = csv2.iloc[0, 1] - value_to_subtract
    
    # Create a new DataFrame with the result
    results_df = pd.concat([results_df, pd.DataFrame({'Index': [i], 'Value': [result_value]})], ignore_index=True)
    
    # Save the result to a new CSV file
    results_df.to_csv('output-ipc-pub-tg.csv', header=False, index=False)
    
    # Optional: print the result of the first row subtraction
    print(f'Result for testzmq-ipc{i} pub-tg:', result_value)
