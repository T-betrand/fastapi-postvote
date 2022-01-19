from fastapi import FastAPI, Response, status, Depends, HTTPException, APIRouter

from sqlalchemy.orm import Session
from typing import List, Optional

from .. import models, schemas, utils
from ..database import engine, get_db



router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def creat_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    #hash password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    check_dublicate = db.query(models.User).filter(models.User.email == user.email).first()
    if check_dublicate:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="user with email already exist")
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(get_db), limit: int = 10, skip: int = 2, search: Optional[str] = ""):
    users = db.query(models.User).filter(models.User.email.contains(search)).limit(limit).offset(skip).all()
    return users

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    return user


@router.put("/update/{id}")
def update_user(id: int, updated_user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} does not exist")
    user_query.update(updated_user.dict(), synchronize_session=False)
    db.commit()
    return user_query.first()


@router.delete("/delete/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if user.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} does not exist")
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)