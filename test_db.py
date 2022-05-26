from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, TransactionIn


engine = create_engine('postgresql+psycopg2://konstantinburmin:holly_1203@localhost/crabs', echo=True)

session = sessionmaker(bind=engine)
s = session()

first_transaction = TransactionIn(product_name='Langust',
                                  size='M',
                                  kilo=1.0,
                                  price_for_kilo=2000,
                                  alive=True,
                                  delivery=True,
                                  coocked=True
                                  )

s.add(first_transaction)
s.commit()