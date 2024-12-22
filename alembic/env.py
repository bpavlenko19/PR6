from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from db import Base  # Підключаємо моделі

# Конфігурація Alembic
config = context.config

# Логування
fileConfig(config.config_file_name)

# Ця змінна має містити всі моделі
target_metadata = Base.metadata

def run_migrations_offline():
    """Запуск міграцій в оффлайн-режимі."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Запуск міграцій в онлайн-режимі."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
