from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserEntity:
    id: int = None
    email: str = None
    password: str = None
    nickname: str = None
    gender: str = None
    join_type: str = None
    is_active: bool = None
    is_block: bool = None
    is_admin: bool = None
    created_at: datetime = None
    updated_at: datetime = None
