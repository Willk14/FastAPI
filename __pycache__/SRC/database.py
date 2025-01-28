from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from . import config

SQL_ALCHEMY_DATABASE_URL = f"postgresql://{config.settings.database_username}:{config.settings.database_password}@{config.settings.database_hostname}:{config.settings.database_port}password123@localhost:8000/fastapi"
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



# Not needed, running raw SQL using the postgres library instead of SQPalchemy
# while True:
#    try:
#        conn = psycopg2.connect(
#            host="localhost",
#            database="fastapi",
#            user="postgres",
#            password="password123",
#            cursor_factory="RealDictCursor",
#        )
#        cursor = conn.cursor()
#        print("Database connection was succesful!")
#    except Exception as error:
#        print("Connection to database has failed")
#        print("Error: error")