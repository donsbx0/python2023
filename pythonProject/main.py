import pandas as pd
import csv


def read_csv_file(file_path):
    """
    Reads a CSV file and returns the header (if it exists) and data as a list of lists.
    """
    # Open the CSV file
    with open(file_path, newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile, delimiter=',')

        # Read the header row (if it exists)
        header = next(reader, None)

        # Create an empty list to hold the data
        data = []

        # Loop through the rows in the CSV file and add them to the list
        for row in reader:
            data.append(row)

    # Return the header (if it exists) and data as a tuple
    return (header, data)



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # file_path = "/Users/don/Downloads/learn.csv"
    file_path = "/Users/don/Desktop/Don/python2023/learn.csv"
    header, data = read_csv_file(file_path=file_path)


    # Get the number of columns
    num_columns = len(header)

    # Extract data from each column and store in a dictionary
    column_data = {}
    for i in range(num_columns):
        column_name = header[i]
        column_data[column_name] = [row[i] for row in data]

    # Print the data from each column
    for column_name, data in column_data.items():
        print(f"Data from column {column_name}: {data}")


