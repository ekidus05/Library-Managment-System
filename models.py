from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

#model of how the Book table should look like in the database
class Book(Base):
    __tablename__="books"
    id = Column(Integer,primary_key = True, index = True)
    
    author_id = Column(Integer,ForeignKey("authors.id"),nullable=False)

    category_id = Column(Integer,ForeignKey("categories.id"),nullable=False)

    title = Column(String)

    author = relationship("Author", back_populates="books")

    category = relationship("Category",back_populates="books")
    # author = Column(String)

#model of how the User table should look like in the database
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True, index = True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable = False, default="member")

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    bio = Column(String,nullable=True)
    books = relationship("Book",back_populates="author")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String,nullable=True)
    books = relationship("Book",back_populates="category")
    