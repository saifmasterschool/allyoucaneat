from usermgmt import *
from api_data_retriever import parse_stock_data
from api_fetch import  *
from data_structure import *
from db_setup import*

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def new_user(ph_num):
    new_user = User(
        phone_number= ph_num,
        stock_of_interest=["AAPL"],
        delivery_frequency= "on_demand",
        delivery_time=None,
        active=True,
        created_at= now(),
        updated_at=now(),
    )
    return new_user




def main():
    API_URL_retrieve_sms = 'http://hackathons.masterschool.com:3030/team/getMessages/WolvesofWallStreet'

    while True:
        user_messages = retrieve_sms(API_URL_retrieve_sms)
        for key, val in user_messages.items():
            len(messages)

    user_messages = retrieve_sms(API_URL_retrieve_sms)

    all_registered_users = user_messages.keys()
    print(all_registered_users)

    #stock_ticker_symbols = "AAPL"
    #api_response = get_stock_data(stock_ticker_symbols)
    #if api_response:
    #    stock_data = parse_stock_data(api_response)
     #   if stock_data:
      #      print(stock_data)


if __name__ == '__main__':
    main()
