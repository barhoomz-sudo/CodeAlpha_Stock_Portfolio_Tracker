def main():
    stocks = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 330}
    
    user_investments = {}
    print(f"Welcome to the Stock tracker App!\nHere's the available stocks:\n{stocks}")
    while True:
        stock_name = input("Enter Stock name (or type 'done' to exit): ").upper().strip()
        if stock_name.lower() == "done":
            break

        if stock_name not in stocks:
            print(f"Sorry, {stock_name} is not in our price list. Please try again")
            continue

        quantity = input("Enter quantity: ")
        if not quantity.isdigit():
            print("Please enter a valid number for quantity")
            continue

        if quantity == "0":
            print("you cant invest $0!")
            continue

        user_investments[stock_name] = user_investments.get(stock_name, 0) + int(quantity)
        
    total = 0
    for key in user_investments:
        value = stocks[key] * user_investments[key]
        total += value
        print(f"Stock name: {key} {user_investments[key]} shares value ${value}")
    print(f"Total investments: {total}")

    save = input("Would you like the results to be saved in a file? (yes/no): ").lower().strip()
    if save == "yes":
        output_file = './results.txt'
        with open(output_file,'w') as f:
            for k in user_investments:
                result = stocks[k] * user_investments[k]
                f.write(f"Stock name: {k} {user_investments[k]} shares value ${result}\n")
            f.write(f"Total investments: ${total}\n")
        print(f"results in -> {output_file}")
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()