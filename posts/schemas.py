from pydantic import BaseModel as Schema, Field
import datetime
from typing import List


class PostIdDetailSchema(Schema):
    pk: int = Field(description="Primary key of post")


class PostDetailSchema(Schema):
    id: int
    title: str
    content: str
    createAt: datetime.datetime
    owner: int
    published: bool


class PostCreateSchema(Schema):
    title: str = Field(description="Title of Post")
    content: str = Field(description="Content of Post")


class ListPostDetailSchema(Schema):
    __root__: List[PostDetailSchema]


class NotFoundSchema(Schema):
    __root__: str = Field("Post is not found")


class DeleteSuccessSchema(Schema):
    __root__: str = Field("Post is Deleted")
