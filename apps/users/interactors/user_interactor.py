from apps.users.repositories import UserMySQLRepository
from apps.users.dtos import CreateUserDto


class UserInteractor:
    def __init__(self):
        self.repository = UserMySQLRepository()


class CreateUserInteractor(UserInteractor):
    def execute(self, dto: CreateUserDto):
        pass
