from sqlalchemy import Column, Integer, String

from .database import Base


class Shortener(Base):
    __tablename__ = "shortener"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    shortcode = Column(String, unique=True, index=True, nullable=False)
