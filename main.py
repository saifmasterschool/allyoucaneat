import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from usermgmt import retrieve_sms
from api_data_retriever import parse_stock_data
from datetime import datetime
from db_setup import initialize, create_database, new_user, update_user, print_all_users
from data_structure import Base, User, Message, Stock

# Constants
api_url_retrieve_sms = 'http://hackathons.masterschool.com:3030/team/getMessages/WolvesofWallStreet'
database_path = os.path.abspath(os.path.join(os.getcwd(), "data", "WoW.sqlite"))

# Initialize the database
initialize(database_path)

# Create the database engine and session
engine = create_engine(f"sqlite:///{database_path}")
Session = sessionmaker(bind=engine)

def main():
    # Create a new session instance
    session = Session()

    while True:
        try:
            # Retrieve SMS messages from the API
            user_messages = retrieve_sms(api_url_retrieve_sms)

            for phone_number, messages in user_messages.items():
                print(f"Phone number {'+' + str(phone_number)} has {len(messages)} messages.")

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
