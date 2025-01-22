import warnings
import logging
import yfinance as yf

from datetime import datetime
from datetime import timedelta
from usermgmt import retrieve_sms


logging.getLogger("yfinance").setLevel(logging.CRITICAL)


def get_date_from_messages(api_url, user_id):
    """Retrieve the date from the last message of a specific user in SMS."""
    messages = retrieve_sms(api_url)
    if not messages:
        print("No messages found.")
        return None

    if user_id not in messages:
        print(f"No messages found for user ID: {user_id}")
        return None

    message_list = messages[user_id]
    if message_list:
        last_message = message_list[-1]
        date_str = last_message.get("text", "").strip()
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print(f"Invalid date format in the last message: {date_str}")
            return None
    else:
        print(f"No messages available for user ID: {user_id}")
        return None


def get_stock_data_yf(stock_symbol, date):
    stock = yf.Ticker(stock_symbol)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")  # Suppress warnings
        for _ in range(5):  # Try up to 5 previous days
            data = stock.history(start=date.strftime("%Y-%m-%d"),
                                 end=(date + timedelta(days=1)).strftime("%Y-%m-%d"))
            if not data.empty:
                return {
                    "Open Price": data.iloc[0]["Open"],
                    "Close Price": data.iloc[0]["Close"],
                    "High Price": data.iloc[0]["High"],
                    "Low Price": data.iloc[0]["Low"],
                }
            date -= timedelta(days=1)  # Fallback to the previous day
        print(f"No stock data available for {stock_symbol} after 5 attempts.")
        return None


def compare_stock_values(stock_symbol, compare_date):
    """Compare stock values from a specific date to today using yfinance."""
    today = datetime.now()
    today_data = get_stock_data_yf(stock_symbol, today)
    compare_date_data = get_stock_data_yf(stock_symbol, compare_date)

    if not today_data:
        print("Unable to fetch stock data for today.")
    if not compare_date_data:
        print("Unable to fetch stock data for the comparison date.")

    if not today_data or not compare_date_data:
        return None

    today_close = today_data.get("Close Price", 0)
    compare_date_close = compare_date_data.get("Close Price", 0)
    difference = round(float(today_close) - float(compare_date_close), 2) \
        if today_close and compare_date_close else "N/A"
    percentage_difference = (
        round((difference / float(compare_date_close)) * 100, 2)
        if difference != "N/A" and compare_date_close
        else "N/A"
    )

    comparison = {
        "Compare Date": compare_date.strftime("%Y-%m-%d"),
        "Today": today.strftime("%Y-%m-%d"),
        "Compare Date Close": compare_date_close,
        "Today Close": today_close,
        "Difference": difference,
        "Percentage Difference": f"{percentage_difference}%" if percentage_difference != "N/A" else "N/A",
    }

    return comparison


if __name__ == "__main__":

#test
    API_URL_retrieve_sms = 'http://hackathons.masterschool.com:3030/team/getMessages/allyoucaneat'
    stock_symbol = "MSFT"

    user_id = "4917640448079"
    compare_date = get_date_from_messages(API_URL_retrieve_sms, user_id)

    if compare_date:
        result = compare_stock_values(stock_symbol, compare_date)

        if result:
            print("Stock Comparison:")
            for key, value in result.items():
                print(f"{key}: {value}")
