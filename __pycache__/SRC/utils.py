# placeholder for hashing
from passlib.context import CryptContext

# Specifies the hashing algorithm to be used
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

# verifies the password
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)