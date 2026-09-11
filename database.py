from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Location of the SQLite database file
DATABASE_URL="sqlite:///./library_managment.db"

#connects SQLALCHEMY to the database file
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

#allows you to create a database session to update the data
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

Base = declarative_base()

#gets that session into the route
def get_db():
  
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
