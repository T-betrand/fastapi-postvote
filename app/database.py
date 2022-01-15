from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip addresse/hostname>/<database_name>'
#'postgresql://<username>:<password>@<ip addresse/hostname>/<database_name>'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base