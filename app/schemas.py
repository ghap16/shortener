from pydantic import BaseModel, HttpUrl


class ShortenerCreate(BaseModel):
    url: HttpUrl


class Shortener(BaseModel):
    id: int
    url: HttpUrl
    shortcode: str

    class Config:
        orm_mode = True
