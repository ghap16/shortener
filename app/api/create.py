from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def create_shortener():
    return {"shorcode": "shortcode_example"}
