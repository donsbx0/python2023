
import pandas as pd
import csv

def summarize_csv_column(csv_file, column_name):
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        column_values = []
        for row in reader:
            column_values.append(float(row[column_name]))
        column_sum = sum(column_values)
    return column_sum



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    csv_file = "/Users/don/Downloads/learn.csv"
    column_sum = summarize_csv_column(csv_file=csv_file,column_name=)
    print(column_sum)




