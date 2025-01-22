from api_fetch import get_stock_data


def parse_stock_data(api_response):
    """Parse and extract stock data from API response."""

    if not api_response or not isinstance(api_response, dict):
        print("Invalid API response: None or not a dictionary.")
        return None

    try:
        stock_attributes = api_response["data"][0]["attributes"]
        last_daily = stock_attributes.get("lastDaily")  # Use `.get` to avoid KeyError

        if not last_daily:
            print("No daily stock data available.")
            return None

        return {
            "Company Name": stock_attributes.get("companyName", "Unknown"),
            "Open Price": last_daily.get("open", "N/A"),
            "Close Price": last_daily.get("close", "N/A"),
            "High Price": last_daily.get("high", "N/A"),
            "Low Price": last_daily.get("low", "N/A"),
            "Current Price": last_daily.get("last", "N/A"),
        }
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error parsing response: {e}")
        return None


# example code
'''symbol = "AAPL"
api_response = get_stock_data(symbol)
if api_response:
    stock_data = parse_stock_data(api_response)
    if stock_data:
        print(stock_data)'''
# end example code
