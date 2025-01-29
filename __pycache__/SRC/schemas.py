from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# Create posts and updateposts handles the direction of the data from user to database
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(PostBase):
   pass

class UpdatePost(PostBase):
    pass

# SQLalchemy model
class userOut(BaseModel):
    id: int
    email: EmailStr
# required to convert to a  pydantic model
    class Config:
        orm_mode = True

#Sending data back to the user

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: userOut
        
    class Config:
        orm_mode = True

class PostOut(PostBase):
    Post: Post
    votes: int
    
    class Config:
        orm_mode = True

class usercreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    Dir = conint(le=1)
    
