from csv_reader import get_data

def get_cash_on_hand(forex):
    # Read csv
    data = get_data("./csv_reports/Cash on Hand.csv")

    f = open("summary_report.txt", "a")

    is_deficit = False

    for i in range(len(data) - 1):
        # Calculate difference for each day
        diff = int(data[i + 1][-1]) - int(data[i][-1])
        # Highlight if difference is negative
        if diff < 0:
            # rounding deficit to 1 decimal place
            coh = round(-diff*forex,1)
            # writing the rounded deficit to the report.txt 
            f.write(f"[CASH DEFICIT] DAY: {data[i + 1][0]}, AMOUNT: SGD{coh}\n")
            is_deficit = True

    # Indicate if no deficit
    if not is_deficit:
        f.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    f.close()