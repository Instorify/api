from enum import Enum, IntEnum
from typing import List, Optional, Union

from instagram_private_api import MediaTypes
from pydantic import BaseModel


class NotFoundMessage(BaseModel):
    detail: str


class InstMediaTypes(IntEnum):
    PHOTO = MediaTypes.PHOTO
    VIDEO = MediaTypes.VIDEO
    CAROUSEL = MediaTypes.CAROUSEL


class Audience(Enum):
    BESTIE = 'besties'


class Location(BaseModel):
    name: str
    lat: float
    lng: float


# Response models

class Story(BaseModel):
    id: int
    type: InstMediaTypes
    audience: Optional[Audience]
    content_url: str
    created_at: int
    duration: Optional[float]
    original_created_at: Optional[int]
    height: int
    width: int
    location: Optional[List[Location]]
    mentions: Optional[List[int]]


class HighlightItemPreview(BaseModel):
    id: int
    preview_url: str
    title: str
    created_at: str
    media_count: int


class User(BaseModel):
    id: int
    username: str
    full_name: str
    profile_img: str
    profile_info: str
    is_private: bool
    is_verified: bool
    follower_count: int
    following_count: int
    media_count: int


class PostPhotoObject(BaseModel):
    type: InstMediaTypes
    height: Optional[int]
    width: Optional[int]
    content_url: str
    mentions: Optional[List[int]]


class PostVideoObject(BaseModel):
    type: InstMediaTypes
    duration: float
    content_url: Optional[str]
    mentions: Optional[List[int]]


PostCarouselList = List[Union[PostPhotoObject, PostVideoObject]]


class Post(BaseModel):
    id: str
    type: InstMediaTypes
    created_at: int
    location: Optional[Location]
    like_count: int
    items: List[Union[PostPhotoObject, PostVideoObject]]
