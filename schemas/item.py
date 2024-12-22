from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True
