from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String, nullable=False, unique=True)
    stock_of_interest = Column(JSON, nullable=False, default=[])
    delivery_frequency = Column(String, nullable=False, default='on_demand')
    delivery_time = Column(String, nullable=False, default='18:00')
    active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False,
                        default=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = Column(DateTime, nullable=False,
                        default=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                        onupdate=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))

    def __repr__(self):
        return (f"<User(id={self.id}, phone_number='{self.phone_number}', "
                f"stock_of_interest={self.stock_of_interest}, delivery_frequency='{self.delivery_frequency}', "
                f"delivery_time='{self.delivery_time}', active={self.active}, "
                f"created_at='{self.created_at}', updated_at='{self.updated_at}')>")


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    type = Column(String, nullable=False)
    date = Column(DateTime, nullable=False,
                  default=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return (f"<Message(id={self.id}, text='{self.text}', "
                f"type='{self.type}', date='{self.date}')>")


class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String, nullable=False)
    open_price = Column(Integer, nullable=False)
    close_price = Column(Integer, nullable=False)
    high_price = Column(Integer, nullable=False)
    low_price = Column(Integer, nullable=False)
    current_price = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False,
                  default=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                  onupdate=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return (f"<Stock(id={self.id}, company_name='{self.company_name}', "
                f"open_price='{self.open_price}', close_price={self.close_price}, "
                f"high_price='{self.high_price}', low_price={self.low_price}, "
                f"current_price='{self.current_price}', date='{self.date}')>")