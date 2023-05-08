from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from working_suntel.config import DB_NAME, DB_HOST, DB_PASSWORD, DB_USER


SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}:{DB_HOST}/{DB_NAME}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
