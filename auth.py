from fastapi import APIRouter,Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
import utils
from database import get_db
import oauth2
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth",tags=["Authentication"])

#the purpose of this post function is to register a new user in the system if they have not been
@router.post("/register",response_model=schemas.UserResponse,status_code=status.HTTP_201_CREATED)

#checks if the user the user exists and if the user does not exist, he will create a email
#and password
def register(user: schemas.UserCreate,db: Session=Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email==user.email).first()

    #if user exists then that means registration gets blocked
    if existing_user:
        raise HTTPException(status_code=400,detail="Email already exists")
    
    #otherwise we hash the users password
    hashed_password = utils.hash(user.password)

    #users info gets added to the library's database
    new_user = models.User(username = user.username,email = user.email,hashed_password = hashed_password,role = user.role)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login",response_model = schemas.Token)
def login(form_data:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email== form_data.username).first()
    
    #if user is not registered then he cannot login
    if not db_user:
        raise HTTPException(status_code=401,detail = "Invalid email or password")
    
    #if the email does not match with the password
    if not utils.verify(form_data.password,db_user.hashed_password):
        raise HTTPException(status_code=401,detail = "Invalid email or password")

    access_token = oauth2.create_access_token(
        data = {
            "user_id":db_user.id
        }
    )
    ##otherwise the login was successful
    return{
        "access_token":access_token,
        "token_type": "bearer"
    }


@router.get("/me")
def get_me(current_user = Depends(oauth2.get_current_user)):
    return current_user


@router.get("/admin")
def admin_test(current_user = Depends(oauth2.require_admin)):
    return{
        "message": "Welcome Admin",
        "username": current_user.username
    }