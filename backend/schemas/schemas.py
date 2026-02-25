from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator
from typing_extensions import Self


class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    password_repeat: str
    is_admin: bool = False
    
    
    
    @model_validator(mode='after')
    def check_if_passwords_match(self) -> Self:
        if self.password != self.password_repeat:
            raise ValueError("Passwords don't match.")
        return self
        

class Admin(UserCreate):
    is_admin = True
    
 
