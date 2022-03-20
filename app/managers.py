from sqlalchemy.orm import Session

from . import models, schemas, utils


def get_shortener_by_shortcode(db: Session, shortcode: str):
    return (
        db.query(models.Shortener)
        .filter(models.Shortener.shortcode == shortcode)
        .first()
    )


def create_shortener(db: Session, shortener: schemas.ShortenerCreate):
    shortcode = utils.generate_shortcode(shortener.url)
    db_shortener = get_shortener_by_shortcode(db, shortcode)
    if db_shortener is None:
        db_shortener = models.Shortener(url=shortener.url, shortcode=shortcode)
        db.add(db_shortener)
        db.commit()
        db.refresh(db_shortener)
    return db_shortener
