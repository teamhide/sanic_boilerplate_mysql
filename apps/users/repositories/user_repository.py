import abc
from typing import Union, NoReturn, List, Optional
from apps.users.entities import UserEntity


class UserRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def save_user(self, query: dict) -> Optional[NoReturn]:
        pass

    @abc.abstractmethod
    def get_user(self, user_id: int) -> Union[UserEntity, NoReturn]:
        pass

    @abc.abstractmethod
    def get_user_list(self) -> Union[List[UserEntity], NoReturn]:
        pass

    @abc.abstractmethod
    def update_user(self, user_id: int, query: dict) -> Optional[NoReturn]:
        pass


class UserMySQLRepository(UserRepository):
    def save_user(self, query: dict) -> Optional[NoReturn]:
        pass

    def get_user(self, user_id: int) -> Union[UserEntity, NoReturn]:
        pass

    def get_user_list(self) -> Union[List[UserEntity], NoReturn]:
        pass

    def update_user(self, user_id: int, query: dict) -> Optional[NoReturn]:
        pass
