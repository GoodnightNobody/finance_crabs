from peewee import *
from config import *

dbhandle = PostgresqlDatabase(db_name, user=user, password=password, host='localhost')
