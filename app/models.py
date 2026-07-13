from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base


class UserForm(Base):

    __tablename__ = "userData"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True)
    email = Column(String(200))
    message = Column(String(200))
