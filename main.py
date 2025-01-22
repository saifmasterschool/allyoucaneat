import os
import time
from pyexpat.errors import messages

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from usermgmt import retrieve_sms, send_sms, unregister_number
from db_setup import initialize, create_database, new_user, update_user, print_all_users
from data_structure import Base, User, Message, Stock
from api_data_retriever import *

# Constants
api_url_retrieve_sms = 'http://hackathons.masterschool.com:3030/team/getMessages/WolvesofWallStreet'
api_url_send_sms = 'http://hackathons.masterschool.com:3030/sms/send'
database_path = os.path.abspath(os.path.join(os.getcwd(), "data", "WoW.sqlite"))

# Initialize the database
initialize(database_path)

# Create the database engine and session
engine = create_engine(f"sqlite:///{database_path}")
Session = sessionmaker(bind=engine)

def send_option(api_url_send_sms, ph_num, text):

    if text.lower().strip() == "unsubscribe":
        unregister_number(ph_num)
        message = "Sucessfully unsubscribed"
        send_sms(api_url_send_sms,ph_num, message)
    elif text.lower().strip() == "stock":
        symbol = "AAPL"
        api_response = get_stock_data(symbol)
        if api_response:
            stock_data = parse_stock_data(api_response)
        message = f"Your Stock 'APPL' has a current value of  ${stock_data['Current Price']}"
        print(message)
        send_sms(api_url_send_sms,ph_num, message)
    else:
        message = "1.Enter 'STOCK': To get Stock info or Enter 'SUBSCRIBE': To cancel subscription"
        send_sms(api_url_send_sms,ph_num, message)



def update_received_messages(self, new_message_count, session):
    """
    Compares the current received messages with the new message count.
    If the count has increased, updates the user's record and returns True.
    If not, returns False.
    """
    if new_message_count > self.num_received_messages:
        self.num_received_messages = new_message_count
        session.commit()
        return True
    return False

def main():
    # Create a new session instance
    session = Session()

    while True:
        try:
            # Retrieve SMS messages from the API
            user_messages = retrieve_sms(api_url_retrieve_sms)


            for phone_number, messages in user_messages.items():
                current_message_count = len(messages)
                print(f"Phone number {'+' + str(phone_number)} has {current_message_count} messages.")

                # Query the User table for the current phone number
                user = session.query(User).filter_by(phone_number=phone_number).first()

                if not user:
                    print(f"No user found for phone number {phone_number}. Creating a new user...")
                    # Call new_user function
                    new_user(session, ph_num=phone_number)
                    session.commit()
                    print(f"New user created for phone number {phone_number}.")
                else:
                    print(f"User found: {user.phone_number}")

                if update_received_messages(user, current_message_count, session):
                    print('New message received!"')
                    time.sleep(2)
                    send_option(api_url_send_sms, '+' + user.phone_number, messages[-1]['text'])

                else:
                    print('No new message received!"')


            # Print all users for debugging
            print_all_users(database_path)

            # Sleep for 5 seconds before fetching again
            time.sleep(5)

        except Exception as e:
            print(f"Error processing user messages: {e}")
            break

        finally:
            # Close the session to release resources
            session.close()

if __name__ == '__main__':
    main()
