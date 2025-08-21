from fastapi import FastAPI, status
from pydantic import Field, BaseModel, field_validator, EmailStr
from uuid import UUID, uuid4

app = FastAPI()


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=5, max_length=12)
    age: int = Field(gt=18, lt=100)

    class Config: # to show this as the placholder in POST request on swagger
        json_schema_extra = {
            'example': {
                'email': 'test@mail.com',
                'password': 'testing123',
                'age': 23
            }
        }

    @field_validator('password')
    def password_validator(cls, value):
        if value == 'testing123':
            raise ValueError("Please do not use default password")
        return value
    

class User(UserCreate):
    id: UUID = Field(default_factory=uuid4)


@app.post('/users/', response_model=User, status_code=status.HTTP_201_CREATED)
def create_users(user: UserCreate):
    created_user = User(**user.model_dump())
    return created_user