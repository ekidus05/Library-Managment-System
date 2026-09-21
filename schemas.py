from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum

class AuthorShort(BaseModel):
    id:int
    name:str
    
    class Config:
        from_attributes = True


class CategoryShort(BaseModel):
    id:int
    name:str

    class Config:
        from_attributes = True



class BookCreate(BaseModel):
    title:str
    author_id:int
    category_id:int

class BookResponse(BaseModel):
    id:int
    title:str
    author:AuthorShort
    category:CategoryShort
    
    class Config:
        from_attributes = True

#blueprint for registering user
class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str
    role:str

#blueprint for the user to log in
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserRole(str, Enum):
    admin = "admin"
    librarian = "librarian"
    member = "member"

#blueprint for fast api to send back to the user
class UserResponse(BaseModel):
    id:int
    username:str
    email:EmailStr
    role: UserRole

    class Config:
        from_attributes = True


class UserRoleUpdate(BaseModel):
    role : UserRole


#used to show the token in fast api server
class Token(BaseModel):
    access_token: str
    token_type:str

#used to identify the token
class TokenData(BaseModel):
    id:int|None = None

class AuthorCreate(BaseModel):
    name:str
    bio:str|None = None

class AuthorResponse(BaseModel):
    id: int
    name: str
    bio : str | None = None

    class Config:
        from_attributes = True



class CategoryCreate(BaseModel):
    name:str
    description:str | None = None


class CategoryResponse(BaseModel):
    id:int
    name:str
    description:str | None = None

    class Config:
        from_attributes = True

class BorrowingCreate(BaseModel):
    book_id:int
    due_date:datetime

class BorrowingResponse(BaseModel):
    id:int
    user_id: int
    book_id: int
    borrow_date: datetime
    due_date: datetime
    return_date: datetime | None = None
    status: str

    class Config:
        from_attributes = True


class BorrowingWithBook(BaseModel):
    id:int
    user_id: int
    book_id: int
    borrow_date: datetime
    due_date: datetime
    return_date: datetime | None = None
    status: str
    book: BookResponse

    class Config:
        from_attributes = True





    