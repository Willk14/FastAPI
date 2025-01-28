from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from ..import models, schemas, utils, database, oAuth

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db), response_model=schemas.Token ):
    # making requests to our database
    # checks if user exists and seeing if the password is correct
    # {
    #     "username": "string",
    #     "password": "string"  
    #}
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User with email: {user_credentials.email} not found")

    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials" )
    
    # create a token
    # return tha token
    access_token = oAuth.create_access_token(data = {"user_id": user.id})
    return {"access_token": access_token , "token_type":"bearer"}