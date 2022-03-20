from hashlib import blake2b

from .database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_shortcode(url):
    url_hash = blake2b(key=url.encode("utf-8"), digest_size=4)
    return url_hash.hexdigest()
