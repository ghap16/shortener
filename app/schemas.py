from pydantic import BaseModel, HttpUrl


class ShortenerCreate(BaseModel):
    url: HttpUrl
