from .database import Base
from sqlalchemy import Column, TIMESTAMP, text, ForeignKey, Integer, String, Boolean, relationship


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

    owner_id = Column(Integer, ForeignKey('users.id'), ondelete="CASCADE", nullable=False)

    # Relationship to fetch some type of information
    owner = relationship("User")
    # return new owner property and figure out the relationship to user

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True))
    phone_number = Column(String)

class Vote(Base):
    __tabkename__ = "user"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade",primary_key=True), nullable=False)
    post_id = Column(Integer, ForeignKey("users.id", ondelete="cascade",primary_key=True), nullable=False)

