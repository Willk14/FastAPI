from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from httpx import post
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2 import RealDictCursor



app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

try:
    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='password123', cursor_factory='RealDictCursor')
    cursor = conn.cursor()
    print("Database connection was succesful!")
except Exception as error:
    print("Connection to database has failed")
    print("Error: error")

   

my_posts = [{"title": "title of post 1", "content":"content of post 1", "id": 1},{"title":"favorite foods","content": "I like pizza", "id":2} ]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
          return p

def find_index_post(id):
    for index, p in enumerate(my_posts):
        if p['id'] == id:
            return index
   

@app.post("/posts")
def create_posts(new_posts: post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post.dict())
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_posts(id: int):

 post = find_post(id)
 if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f"post with id: {id} was not found") 
 return {"post_detail": post}

@app.get("/posts/{id}")
def get_post(id: int):
    print(type(id))
    post = find_post(id)
    print(post)
    return{"post_details": post }

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    # deleting posts
    # finding the index in the array that has required ID
    # my_posts.pop(index)
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"post with id{id} does not exist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist") 
        
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {'message': 'updated post'}

