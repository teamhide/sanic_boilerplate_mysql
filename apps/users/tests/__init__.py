import pytest
from apps.users.repositories import UserMySQLRepository
from apps.users.interactors import CreateUserInteractor


@pytest.fixture
def repository():
    return UserMySQLRepository()


@pytest.fixture
def create_user_interactor():
    return CreateUserInteractor
