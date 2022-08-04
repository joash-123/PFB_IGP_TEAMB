import api, profit_loss,cash_on_hand,overheads


def main():

    forex = api.CURRENCY_EXCHANGE_RATE()
    api.get_conversion_rate()
    overheads.get_overheads(forex)
    cash_on_hand.get_cash_on_hand(forex)
    profit_loss.get_profit_loss(forex)

print(main())

from pathlib import Path
#creating a new text document named: team_members.txt
file_path = Path.cwd()/"team_members.txt"
file_path.touch()

with file_path.open(mode="w", encoding="UTF-8") as file:
    # inputing our names and student IDs into team_members.txt
    file.write("LEE ZAN HUA JOASH, S10220929\nKOH RUI AN, S10242046\nNEVIN JOBY, S10243461\nJEREMY FOO GENG RONG, S10243326\nSUFFIAN ABDULLAH, S10221009")