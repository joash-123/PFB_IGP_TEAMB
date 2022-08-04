from csv_reader import get_data

def get_profit_loss(forex):
    # Read csv
    data = get_data("./csv_reports/Profit-and-loss.csv")

    f = open("summary_report.txt", "a")

    is_deficit = False

    for i in range(len(data) - 1):
        # Calculate difference for each day
        diff = int(data[i + 1][-1]) - int(data[i][-1])
        # Highlight if difference is negative
        if diff < 0:
            test = round(-diff*forex,1)
            f.write(f"[PROFIT DEFICIT] DAY: {data[i + 1][0]}, AMOUNT: SGD{test}\n")
            is_deficit = True

    # Indicate if no deficit
    if not is_deficit:
        f.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    f.close()