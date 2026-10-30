from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from database.connection import get_session
from models.users import User, UserSignIn, NewUser

user_router = APIRouter(tags=["User"])

@user_router.post("/signup", status_code=201)
async def sign_new_user(new_user: NewUser, session=Depends(get_session)) -> dict:
    statement = select(User).where(User.email == new_user.email)
    existing_user = session.exec(statement).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email exists"
        )
    
    user = User(
        email=new_user.email,
        password=new_user.password,
        username=new_user.username
    )
    
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return {"message": "User successfully registered!"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn, session=Depends(get_session)) -> dict:
    statement = select(User).where(User.email == user.email)
    existing_user = session.exec(statement).first()
    
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    
    if existing_user.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )
    
    return {"message": "User signed in successfully"}