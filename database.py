import os
import datetime as dt

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# PostgreSQL connection
DATABASE_URL_local = "postgresql+psycopg2://postgres:mmarpsql%402003@localhost:5432/hospital_appointments"

DATABASE_URL = os.getenv("DATABASE_URL", DATABASE_URL_local)  # Use environment variable if available, else use local URL

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not configured")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


class Appointment(Base):
    __tablename__ = "appointments"

    Appointment_id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, index=True)
    reason = Column(String, nullable=True)
    start_time = Column(DateTime, index=True)
    cancelled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=dt.datetime.utcnow)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()