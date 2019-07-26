from datetime import datetime
from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.BigIntField(pk=True)
    email = fields.CharField(max_length=50)
    password = fields.CharField(max_length=80)
    nickname = fields.CharField(max_length=20)
    gender = fields.CharField(max_length=2)
    join_type = fields.CharField(max_length=20, default='default')
    is_active = fields.BooleanField()
    is_block = fields.BooleanField()
    is_admin = fields.BooleanField()
    created_at = fields.DatetimeField(default=datetime.now().replace(microsecond=0))
    updated_at = fields.DatetimeField(default=datetime.now().replace(microsecond=0))

    class Meta:
        table = 'users'
