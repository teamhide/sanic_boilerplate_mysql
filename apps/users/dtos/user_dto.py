from dataclasses import dataclass


@dataclass
class RegisterUserDto:
    email: str = None
    password1: str = None
    password2: str = None
    nickname: str = None
    gender: str = None
    join_type: str = None
