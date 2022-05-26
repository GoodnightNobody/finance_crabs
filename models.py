import datetime

from sqlalchemy import Column, create_engine, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg2://konstantinburmin:holly_1203@localhost/crabs', echo=True)
Base = declarative_base()


class TransactionIn(Base):
    __tablename__ = 'transactions_in'

    id_transaction = Column(Integer, primary_key=True)
    product_name = Column(String(250), nullable=False)
    size = Column(String(1), nullable=False)
    kilo = Column(Float, nullable=False)
    price_for_kilo = Column(Float, nullable=False)
    alive = Column(Boolean, nullable=False)
    delivery = Column(Boolean, nullable=False)
    coocked = Column(Boolean, nullable=False)
    date_time = Column(DateTime, default=datetime.datetime.utcnow(), nullable=False)


Base.metadata.create_all(engine)
