from __future__ import annotations

import os
from typing import Generator

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    load_dotenv = None

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

if load_dotenv is not None:
    load_dotenv()

DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./bussola.db")

engine: Engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal: sessionmaker[Session] = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)

Base = declarative_base()


def get_session() -> Generator[Session, None, None]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
