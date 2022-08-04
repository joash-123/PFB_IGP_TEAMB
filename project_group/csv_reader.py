import csv

def get_data(fname):
    openfile = open(fname)
    csvreader = csv.reader(openfile)

    next(csvreader)  # Skip column names
    data = []
    for row in csvreader:
        data.append(row)
    
    return data