import api, profit_loss,cash_on_hand,overheads


def main():

    forex = api.CURRENCY_EXCHANGE_RATE()
    api.get_conversion_rate()
    overheads.get_overheads(forex)
    cash_on_hand.get_cash_on_hand(forex)
    profit_loss.get_profit_loss(forex)

print(main())