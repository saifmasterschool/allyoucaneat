from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

from data_structure import  Base, User, Message, Stock
import os


def create_database(db_url):
    """
    Create database tables based on the SQLAlchemy ORM models.

    Args:
        db_url (str): Database connection URL (e.g., 'sqlite:///my_database.db').
    """
    # Create an engine for the database
    engine = create_engine(db_url)

    # Create all tables defined in the Base
    Base.metadata.create_all(engine)

    print("Database tables created successfully.")

def initialize(database_path):
    """
    Initializes the database connection and returns a sessionmaker.
    """
    # Correct format for SQLite database URL
    database_url = f"sqlite:///{database_path}"

    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)  # Create all tables if not already created
    return Session


def print_all_users(database_path):
    """
    Opens the database and prints all entries in the User table.

    Args:
        database_path (str): Path to the SQLite database.
    """
    # Create the database URL
    database_url = f"sqlite:///{database_path}"

    # Create the engine and session
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query all users
        users = session.query(User).all()

        if users:
            print("Users in the database:")
            for user in users:
                print(user)
        else:
            print("No users found in the database.")

    except Exception as e:
        print(f"Error querying the database: {e}")
    finally:
        # Close the session
        session.close()


def new_user(session, ph_num, num_received_messages=0):
    """
    Creates a new user and adds them to the database.
    """
    new_user = User(
        phone_number=ph_num,
        stock_of_interest="AAPL",
        num_received_messages=num_received_messages,
        num_sent_messages=0,
        delivery_frequency="on_demand",
        delivery_time=None,
        active=True,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    try:
        session.add(new_user)
        session.commit()
        print(f"User with phone number {ph_num} added successfully.")
    except IntegrityError:
        session.rollback()
        print(f"User with phone number {ph_num} already exists.")
    except Exception as e:
        session.rollback()
        print(f"Error adding user: {e}")


# Function to update user details
def update_user(session, ph_num, **kwargs):
    """
    Updates an existing user's details. Pass the phone number of the user to update
    along with keyword arguments for fields to update.
    """
    user = session.query(User).filter_by(phone_number=ph_num).first()
    if not user:
        print(f"No user found with phone number {ph_num}.")
        return

    for key, value in kwargs.items():
        if hasattr(user, key):
            setattr(user, key, value)
            user.updated_at = datetime.now()  # Update timestamp
        else:
            print(f"Invalid field: {key}")

    try:
        session.commit()
        print(f"User with phone number {ph_num} updated successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error updating user: {e}")

def test_database():
    database_path = os.path.join(os.getcwd(), "data", "WoW.sqlite")
    os.makedirs(os.path.dirname(database_path), exist_ok=True)

    # Step 1: Create the database
    print("Creating database...")
    create_database(f"sqlite:///{database_path}")

    # Step 2: Initialize a session
    print("Initializing database...")
    Session = initialize(database_path)
    session = Session()

    # Step 3: Test adding a user
    print("Adding a test user...")
    new_user(session, ph_num="1234567890")

    # Step 4: Test updating the user
    print("Updating the test user...")
    update_user(session, ph_num="1234567890", stock_of_interest="GOOGL")

    # Verify user
    user = session.query(User).filter_by(phone_number="1234567890").first()
    if user:
        print(f"User found: {user}")
    else:
        print("User not found.")

    session.close()

if __name__ == "__main__":
    test_database()