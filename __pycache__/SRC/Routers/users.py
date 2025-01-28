from fastapi import fastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..import models, schemas, utils
from ..database import get_db
from typing import List


router = APIRouter(
    prefix="/users",
    tags=['Users']
)


@router.post("/{id}", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.Usercreate, db: Session = Depends(get_db), response_model=schemas.userOut):
#Hash the password

    hashed_password = utils.hash(user.password)

    # update pydantic model to SQL model
    # user.password is an attrinute of the user model
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Route to retrieve information about the user
@router.get('/users/{id}',  response_model=schemas.userOut)
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} was not found")