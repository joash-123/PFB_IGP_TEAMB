from csv_reader import get_data

def get_overheads(forex):
    # Read csv
    data = get_data("./csv_reports/Overheads.csv")

    f = open("summary_report.txt", "a")
    f.write("[HIGHEST OVERHEAD] ")

    # Save all overhead values into a single list
    values = []
    for row in data:
        values.append(float(row[-1]))
    
    # Find the highest overhead value
    max_overhead = max(values)
    # Get category name of the highest value
    max_index = values.index(max_overhead)
    category = data[max_index][0].upper()
    # rounding the flagged overhead to 1 decimal point
    finalamount = round((float(max_overhead)*forex),1)
    # writing the rounded flagged overhead to the report.txt
    f.write(f"{category}: SGD{finalamount}\n")
    f.close()