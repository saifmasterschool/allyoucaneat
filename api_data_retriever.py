from api_fetch import get_stock_data


def parse_stock_data(api_response):
    """Parse and extract stock data from API response."""
    try:
        stock_attributes = api_response["data"][0]["attributes"]
        last_daily = stock_attributes["lastDaily"]

        return {
            "Company Name": stock_attributes["companyName"],
            "Open Price": last_daily["open"],
            "Close Price": last_daily["close"],
            "High Price": last_daily["high"],
            "Low Price": last_daily["low"],
            "Current Price": last_daily["last"],
        }
    except (KeyError, IndexError) as e:
        print(f"Error parsing response: {e}")
        return None

def main():# example code
    symbol = "AAPL"
    api_response = get_stock_data(symbol)
    if api_response:
        stock_data = parse_stock_data(api_response)
        if stock_data:
            print(stock_data)

if __name__ == "__main__":
    main()