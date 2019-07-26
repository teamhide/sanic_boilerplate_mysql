from marshmallow import fields
from core.schemas import BaseSchema


# Request Schemas
class CreateUserRequestSchema(BaseSchema):
    email = fields.Email(required=True)
    password1 = fields.Str(required=True)
    password2 = fields.Str()
    nickname = fields.Str(required=True)
    gender = fields.Str(required=True)
    join_type = fields.Str(required=True)


# Response Schemas
class UserResponseSchema(BaseSchema):
    email = fields.Email()
    nickname = fields.Str()
    gender = fields.Str()
