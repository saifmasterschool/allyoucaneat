import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("API_KEY")

# Mark's code
def get_stock_data(stock_id):
    """Get stock profile data for a given stock ID."""
    url = "https://seeking-alpha.p.rapidapi.com/symbols/get-profile"

    querystring = {"symbols": stock_id}

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
#end Mark's code


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


# example code to test
symbol = "AAPL"
api_response = get_stock_data(symbol)
if api_response:
    stock_data = parse_stock_data(api_response)
    if stock_data:
        print(stock_data)
# end example code
