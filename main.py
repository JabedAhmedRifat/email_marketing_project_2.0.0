import csv

# Specify the filename for your CSV file
filename = 'data.csv'

# Define the column names
columns = ['gmail', 'phone', 'name']

# Define the dummy data
dummy_data = [
    ['dummy@gmail.com', '1234567890', 'John Doe'],
    ['example@gmail.com', '9876543210', 'Jane Smith'],
]

# Create a CSV file, write the header row, and fill with dummy data
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns)  # Write the header row
    writer.writerows(dummy_data)  # Write the dummy data rows

print(f'CSV file "{filename}" with columns "gmail," "phone," and "name" has been created with dummy data.')
