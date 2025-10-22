from pydantic import BaseModel,Field, EmailStr,field_validator

class SysUserDTO(BaseModel):
    username:str = Field(...,min_length=2,max_length=50,description="Username of the system user")
    email:EmailStr = Field(...,description="Email address of the system user")
    full_name:str = Field(...,min_length=2,max_length=100,description="Full name of the system user")
    password:str = Field(...,min_length=6,max_length=100,description="Password for the system user")

    @field_validator('username')
    def username_must_not_contain_spaces(cls, v):
        if ' ' in v:
            raise ValueError('Username must not contain spaces')
        return v
    
    @field_validator('password')
    def password_must_be_strong(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(char in '!@#$%^&*()-+' for char in v):
            raise ValueError('Password must contain at least one special character (!@#$%^&*()-+)')
        return v
