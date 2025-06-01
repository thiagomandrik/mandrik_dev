from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    email: str
    password: str


class UserPublicSchema(BaseModel):
    username: str
    email: str
