from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time,  psycopg2
from psycopg2.extras import RealDictCursor


SQLALCHEMY_DATABASE_URL = 'postgresql://tebo:Dream-Land2@localhost/fastapi'
#'postgresql://<username>:<password>@<ip addresse/hostname>/<database_name>'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# while True:

#     try:
#         conn =  psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'tebo', password = 'Dream-Land2', cursor_factory= RealDictCursor)
#         cursor = conn.cursor()
#         print('database connection was successfull')
#     except Exception as error:
#         print('connection to database failed')
#         print("Error: ", error)
#         time.sleep(2)