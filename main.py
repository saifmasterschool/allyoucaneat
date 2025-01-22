import time
from usermgmt import *
from api_data_retriever import parse_stock_data
from api_fetch import  *
#from data_structure import *
from db_setup import*



def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    # Database path
    database_path = "/data/WoW.sqlite"

    # Initialize the database and create a session
    Session = initialize(database_path)
    session = Session()
    while True:
        try:
            # Fetch the data directly
            user_messages = retrieve_sms(api_url_retrieve_sms)

            for phone_number, messages in user_messages.items():
                print(f"Phone number {phone_number} has {len(messages)} messages.")

                # Check if the user exists in the database
                user = session.query(User).filter_by(phone_number=phone_number).first()

                if user:
                    # Update the user's received message count
                    update_user(
                        session,
                        ph_num=phone_number,
                        num_received_messages=user.num_received_messages + len(messages)
                    )
                else:
                    # If user doesn't exist, create a new user
                    print(f"Phone number {phone_number} not found. Creating new user.")
                    new_user(session, phone_number)

            # Sleep for 5 seconds before fetching again
            time.sleep(5)

        except Exception as e:
            print(f"Error processing user messages: {e}")
            break


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
