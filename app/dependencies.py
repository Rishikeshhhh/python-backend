from fastapi import Header, HTTPException, Depends
from .token import SECRET_KEY, ALGORITHM
from jose import jwt, JWTError
from .crud.user import retrieve_user

async def get_current_user(token: str = Header(...)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await retrieve_user(email)
    if user is None:
        raise credentials_exception
    return user
