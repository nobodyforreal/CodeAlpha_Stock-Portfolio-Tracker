import yfinance as yf

portfolio = {}

def add_stock():
    symbol = input("Enter stock symbol (e.g. AAPL): ").upper()
    quantity = int(input("Enter quantity: "))
    buy_price = float(input("Enter purchase price per share: "))
    
    portfolio[symbol] = {
        "quantity": quantity,
        "buy_price": buy_price
    }
    print(f"{symbol} added to portfolio.\n")

def remove_stock():
    symbol = input("Enter stock symbol to remove: ").upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed.\n")
    else:
        print("Stock not found in portfolio.\n")

def view_portfolio():
    if not portfolio:
        print("Portfolio is empty.\n")
        return

    print("\nYour Portfolio:")
    total_invested = 0
    total_value = 0

    for symbol, data in portfolio.items():
        stock = yf.Ticker(symbol)
        current_price = stock.history(period="1d")["Close"][-1]

        quantity = data["quantity"]
        buy_price = data["buy_price"]
        invested = quantity * buy_price
        current_val = quantity * current_price
        profit = current_val - invested

        total_invested += invested
        total_value += current_val

        print(f"\n{symbol}:")
        print(f"  Quantity: {quantity}")
        print(f"  Buy Price: ${buy_price:.2f}")
        print(f"  Current Price: ${current_price:.2f}")
        print(f"  Invested: ${invested:.2f}")
        print(f"  Current Value: ${current_val:.2f}")
        print(f"  Profit/Loss: ${profit:.2f}")

    print("\nSummary:")
    print(f"  Total Invested: ${total_invested:.2f}")
    print(f"  Total Current Value: ${total_value:.2f}")
    print(f"  Overall Gain/Loss: ${total_value - total_invested:.2f}\n")

def menu():
    while True:
        print("===== Stock Portfolio Tracker =====")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_stock()
        elif choice == '2':
            remove_stock()
        elif choice == '3':
            view_portfolio()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
