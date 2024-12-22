import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.item import Item

DATABASE_URL = "postgres://baza"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Вставка 1000 записів
start_time = time.time()
for i in range(1000):
    db.add(User(username=f'user{i}', email=f'user{i}@example.com', password_hash='password123'))
db.commit()
print(f"Insert 1000 users: {time.time() - start_time} seconds")

# Вибірка 1000 записів
start_time = time.time()
users = db.query(User).filter(User.username == 'user100').all()  # Використовуємо індекс на username
print(f"Select 1000 users: {time.time() - start_time} seconds")

# Оновлення 1000 записів
start_time = time.time()
for user in users:
    user.password_hash = 'newpassword'
db.commit()
print(f"Update 1000 users: {time.time() - start_time} seconds")

# Видалення 1000 записів
start_time = time.time()
for user in users:
    db.delete(user)
db.commit()
print(f"Delete 1000 users: {time.time() - start_time} seconds")
