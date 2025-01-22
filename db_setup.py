from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_structure import  Base, User, Message, Stock
import uuid_utils as uuid

# Create a database connection
engine = create_engine('sqlite:///data/WoW.sqlite')

# Create a database session
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def add_item(session, model, **kwargs):
    new_record = model(**kwargs)
    session.add(new_record)
    session.commit()
    print(f"Added: {new_record}")


def delete_item(session, model, record_id):
    record_to_delete = session.query(model).get(record_id)
    if record_to_delete:
        session.delete(record_to_delete)
        session.commit()
        print(f"Deleted: {record_to_delete}")
    else:
        print(f"Record with ID {record_id} not found.")


def update_record(session, model, record_id, **kwargs):
    record_to_update = session.query(model).get(record_id)
    if record_to_update:
        for key, value in kwargs.items():
            setattr(record_to_update, key, value)
        session.commit()
        print(f"Updated: {record_to_update}")
    else:
        print(f"Record with ID {record_id} not found.")


def get_user_by_phone_number(session, model, phone_number):
    record = session.query(model).filter(model.phone_number == phone_number).first()
    if record:
        return record
    else:
        print(f"No record found with phone_number: {phone_number}")
        return None