from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import managers, schemas
from ..utils import get_db

router = APIRouter()


@router.get("/{shortcode}", response_model=schemas.Shortener)
def read_shortener(shortcode: str, db: Session = Depends(get_db)):
    db_shortener = managers.get_shortener_by_shortcode(db, shortcode=shortcode)
    if db_shortener is None:
        raise HTTPException(status_code=404, detail="Shortener not found")
    return db_shortener
