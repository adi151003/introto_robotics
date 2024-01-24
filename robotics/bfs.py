import csv

# Open the CSV file in read mode
with open('epl_results_2022-23.csv', 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    
    # Iterate through each row in the CSV file
    for row in csvreader:
        # Print each row as a table row
        print('\t'.join(row))