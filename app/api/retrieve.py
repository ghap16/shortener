from fastapi import APIRouter
router = APIRouter()


@router.get("/{shortcode}")
def read_shortener(shortcode: str):
    return {"url": "http://example.com"}
