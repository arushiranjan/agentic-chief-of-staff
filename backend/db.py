from sqlalchemy import create_engine, Column, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://agent:agentpass@localhost:5432/agentdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Memory(Base):
    __tablename__ = "memory"

    user_id = Column(String, primary_key=True)
    key = Column(String, primary_key=True)
    value = Column(Text)

def init_db():
    Base.metadata.create_all(bind=engine)
