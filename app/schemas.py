from pydantic import BaseModel, EmailStr


class UserformSchema(BaseModel):
    name: str
    email: str
    message: str


class UserfromSchemaresponse(BaseModel):
    name: str
    email: str
    message: str

    class Config:
        from_attributes = True
