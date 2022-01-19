from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, schemas, models, utils, Oauth2
from sqlalchemy.orm import Session



router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    if not utils.verify(user.password, user_credentials.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="invalid credentials")

    #create token
    access_token = Oauth2.create_access_token(data = {"user_id": user.id})
    return {"access_token": access_token , "token_type": "bearer"}
    #