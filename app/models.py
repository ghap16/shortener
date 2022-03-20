from sqlalchemy import Column, Integer, String

from .database import Base


class Shortener(Base):
    __tablename__ = "shortener"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(2083), nullable=False)
    shortcode = Column(String(8), unique=True, index=True, nullable=False)
