from datetime import datetime
from api_fetch import get_stock_data
from api_data_retriever import parse_stock_data
from usermgmt import retrieve_sms


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


def compare_stock_values(stock_symbol, compare_date, api_url):
    """Compare stock values from a specific date to today."""
    today = datetime.now().strftime("%Y-%m-%d")
    today_data = get_stock_data(stock_symbol)
    today_stock = parse_stock_data(today_data)
    compare_date_data = get_stock_data(stock_symbol)
    compare_date_stock = parse_stock_data(compare_date_data)

    if not today_stock:
        print("Unable to fetch or parse today's stock data.")
    if not compare_date_stock:
        print("Unable to fetch or parse stock data for the comparison date.")

    if not today_stock or not compare_date_stock:
        print(f"Compare Date Data: {compare_date_data}")
        print(f"Today Data: {today_data}")
        return None

    today_close = today_stock.get("Close Price", 0)
    compare_date_close = compare_date_stock.get("Close Price", 0)
    difference = round(float(today_close) - float(compare_date_close), 2) \
        if today_close and compare_date_close else "N/A"
    percentage_difference = (
        round((difference / float(compare_date_close)) * 100, 2)
        if difference != "N/A" and compare_date_close
        else "N/A"
    )

    comparison = {
        "Compare Date": compare_date.strftime("%Y-%m-%d"),
        "Today": today,
        "Compare Date Close": compare_date_close,
        "Today Close": today_close,
        "Difference": difference,
        "Percentage Difference": f"{percentage_difference}%" if percentage_difference != "N/A" else "N/A",
    }

    return comparison


if __name__ == "__main__":

    API_URL_retrieve_sms = 'http://hackathons.masterschool.com:3030/team/getMessages/allyoucaneat'
    stock_symbol = "BTC"

    user_id = "4917640448079"
    compare_date = get_date_from_messages(API_URL_retrieve_sms, user_id)

    if compare_date:
        result = compare_stock_values(stock_symbol, compare_date, API_URL_retrieve_sms)

        if result:
            print("Stock Comparison:")
            for key, value in result.items():
                print(f"{key}: {value}")
