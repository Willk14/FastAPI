from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from httpx import post
from pydantic import BaseSettings
from typing import Optional,List
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import session, Session, sessionmaker
from .Routers import post, users, auth, oAuth, vote
from .import config


models.base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()




app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

