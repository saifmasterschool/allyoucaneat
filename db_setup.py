from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from datetime import datetime, timezone
from data_structure import  Base, User, Message, Stock
import os

Base = declarative_base()


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

def new_user(session, ph_num):
    """
    Creates a new user and adds them to the database.
    """
    new_user = User(
        phone_number=ph_num,
        stock_of_interest="AAPL",
        num_received_messages=0,
        num_sent_messages=0,
        delivery_frequency="on_demand",
        delivery_time=None,
        active=True,
        created_at=now(),
        updated_at=now(),
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
            user.updated_at = now()  # Update timestamp
        else:
            print(f"Invalid field: {key}")

    try:
        session.commit()
        print(f"User with phone number {ph_num} updated successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error updating user: {e}")