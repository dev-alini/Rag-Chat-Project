from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/mydb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def fetch_relevant_rows(query:str, params:dict=None):
    with engine.connect() as conn:
        q = text(query)
        result = conn.execute(q, params or {})
        return [dict(row) for row in result.fetchall()]
