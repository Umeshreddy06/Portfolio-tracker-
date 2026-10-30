# Demonstration prices only; these are not live market prices.
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 170.00,
}


def main():
    portfolio = {}
    print("===== STOCK PORTFOLIO TRACKER =====")
    print("Demo prices only; not current market data.")

    while True:
        stock = input("Enter a stock symbol (or DONE to finish): ").strip().upper()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print("Unknown symbol. Available:", ", ".join(STOCK_PRICES))
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue
        except ValueError:
            print("Please enter a whole number for quantity.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    total = 0.0
    print("\n===== PORTFOLIO SUMMARY =====")
    if not portfolio:
        print("No stocks entered.")
    for stock, quantity in portfolio.items():
        value = STOCK_PRICES[stock] * quantity
        total += value
        print(f"{stock}: {quantity} shares x ${STOCK_PRICES[stock]:.2f} = ${value:.2f}")
    print(f"Total estimated investment: ${total:.2f}")

    save = input("Save summary to portfolio.txt? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.txt", "w", encoding="utf-8") as file:
            file.write("Stock Portfolio Summary\n")
            for stock, quantity in portfolio.items():
                value = STOCK_PRICES[stock] * quantity
                file.write(f"{stock}: {quantity} shares = ${value:.2f}\n")
            file.write(f"Total estimated investment: ${total:.2f}\n")
        print("Saved to portfolio.txt")


if __name__ == "__main__":
    main()
