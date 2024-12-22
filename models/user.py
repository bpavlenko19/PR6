from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Index

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)  # Додаємо індекс на поле id
    username = Column(String, unique=True, index=True)  # Індекс на поле username
    email = Column(String, unique=True, index=True)  # Індекс на поле email
    password_hash = Column(String)

    # Додаємо індекси на поля для швидшої вибірки
    __table_args__ = (
        Index('idx_user_email', 'email'),
        Index('idx_user_username', 'username'),
    )
