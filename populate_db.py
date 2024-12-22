from sqlalchemy.orm import Session
from faker import Faker
from db import engine, get_db
from models.user import User
from models.item import Item

# Генерація фейкових даних
fake = Faker()

def populate_users(db: Session, count: int):
    users = [
        User(username=fake.user_name(), email=fake.email(), password_hash=fake.password())
        for _ in range(count)
    ]
    db.bulk_save_objects(users)
    db.commit()

def populate_items(db: Session, count: int):
    items = [
        Item(name=fake.word(), description=fake.text(), price=round(fake.random_number(digits=2), 2))
        for _ in range(count)
    ]
    db.bulk_save_objects(items)
    db.commit()

def main():
    db = next(get_db())
    
    sizes = [1000, 10000, 100000, 1000000]
    
    for size in sizes:
        print(f"Наповнення бази даних: {size} записів")
        populate_users(db, size)
        populate_items(db, size)
        print(f"База даних успішно наповнена {size} записами")

if __name__ == "__main__":
    main()
