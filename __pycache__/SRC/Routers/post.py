        from fastapi import fastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session, session
from ..import models, schemas, utils, oAuth2, oath2
from ..database import get_db
from typing import List, Optional



router = APIRouter(
    prefix="/posts" , #/id
    tags=['Posts']
)



@router.post("/{id}", status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.CreatePost, response_model=schemas.Post, db: Session = Depends(get_db), user_id: int = Depends(oath2.get_current_user), current_user: int = Depends(oAuth2.get_current_user)):
    
    new_posts = models.post(owner_id=current_user.id,**post.dict())
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)

@router.get("/{id}", response_model=List[schemas.Post])
async def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oAuth2.get_current_user), Limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    print(Limit)
    posts = db.query(models.Post.title.contains(search)).filter(models).limit(Limit).offset(skip).all()
    # When skipping we use the offset functionality
    
    return posts


@router.get("/{id}")
def get_posts(id:int, db: Session = Depends(get_db), current_user: int = Depends(oAuth2.get_current_user)):
    print(current_user.id)
    post = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    # If you don't want to make the posts public
    if post.owner_id != current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Not authorized tp perform requested action")
    
    return post


def new_func(db):
    posts = db.query(models.Post).all()
    return posts


@router.delete("{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(db: session = Depends(get_db), current_user: int = Depends(oAuth2.get_current_user)):
    # deleting posts
    # finding the index in the array that has required ID
    # my_posts.pop(index)
    
    post_query = db.query(models.post).filter(models.post.id == id).first()
    post = post_query.first()
    
    if post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=f"post with id{id} does not exist",
        )
    if post.owner_id != current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Not authorized tp perform requested action")
    
    post.query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("{id}")
def update_post(id: int, updated_post: schemas.updatePost, db:session = Depends(get_db), current_user: int = Depends(oAuth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
  

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist",
        )
    if post.owner_id != current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    post_query.update(updated_post.dict(), synchronized_session=False) 
    db.commit()

    return post_query.first()