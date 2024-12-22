from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import get_db
from models.user import User
from models.item import Item
from schemas.user import UserCreate, User
from schemas.item import ItemCreate, Item

app = FastAPI()

# Реєстрація нового користувача
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, email=user.email, password_hash=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Створення нового товару
@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
