from fastapi import FastAPI, Depends
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

import app.schemas as schemas
import app.models as models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Project")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "FastAPI project running successfully"}


# createUser
@app.post("/user_create")
def CreateUser(user: schemas.UserformSchema, db :Session=Depends(get_db)):
    db_user = models.UserForm(name=user.name, email=user.email, message=user.message)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/v2/user_create")
def usercreatev2(user:schemas.UserformSchema,db:Session=Depends(get_db)):
    db_user=models.UserForm(name=user.name,email=user.email,message=user.message)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user




from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

@app.post("/v3/user_create")
def usercreatev2(user: schemas.UserformSchema, db: Session = Depends(get_db)):
    try:
        db_user = models.UserForm(
            name=user.name,
            email=user.email,
            message=user.message
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    
@app.get("/v1/list", response_model=list[schemas.UserformSchema])
def listouser(db:Session=Depends(get_db)):
    user=db.query(models.UserForm).all()
    return user
