# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# # from app.config import DATABASE_URL

# # ✅ Correct: create_engine returns an Engine object
# DATABASE_URL = "sqlite:///./test.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# # ✅ Correct: bind to the engine, not a function
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()




from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "fast_api"
DB_USER = "tis"
DB_PASSWORD = "tis"

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
