from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import managers, schemas
from ..utils import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Shortener)
def create_shortener(
    shortener: schemas.ShortenerCreate, db: Session = Depends(get_db)
):
    return managers.create_shortener(db=db, shortener=shortener)
