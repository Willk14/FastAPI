from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import session, Session, sessionmaker
from .Routers import post, users, auth, oAuth, vote
from .import config


# with alembic you don't need this command
models.base.metadata.create_all(engine)

app = FastAPI()
#allows for google request
#provide list of urls that can talk to API
origins = ["*"]
#allowing domains to talk to APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

