import requests
import bcrypt
from core.exceptions import PermissionErrorException, InvalidJoinTypeException, SocialLoginFailException
from apps.users.repositories import UserMySQLRepository
from apps.users.dtos import CreateUserDto
from apps.users.entities import UserEntity


class UserInteractor:
    def __init__(self):
        self.repository = UserMySQLRepository()

    async def _create_hash(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return str(bcrypt.hashpw(password=password.encode('utf8'), salt=salt))


class CreateUserInteractor(UserInteractor):
    def __init__(self):
        super().__init__()
        self.kakao_url = ''
        self.facebook_url = ''
        self.headers = {}

    def execute(self, dto: CreateUserDto):
        """
        유저 회원가입 함수
        :param dto: CreateUserDto
        :return: UserEntity|NoReturn
        """

        if dto.password1 != dto.password2:
            raise PermissionErrorException

        if dto.join_type == 'kakao':
            await self._register_by_kakao(dto=dto)
        elif dto.join_type == 'facebook':
            await self._register_by_facebook(dto=dto)
        elif dto.join_type == 'default':
            await self._register_by_default(dto=dto)
        else:
            raise InvalidJoinTypeException

        hashed_password = await self._create_hash(password=dto.password1)

        user_entity = UserEntity(
            email=dto.email,
            password=hashed_password,
            nickname=dto.nickname,
            gender=dto.gender,
            join_type=dto.join_type,
        )

        await self.repository.save_user(entity=user_entity)
        return user_entity

    async def _register_by_kakao(self, dto: CreateUserDto) -> bool:
        # TODO: 소셜 로그인 연동 필요
        data = {'email': dto.email, 'password': dto.password1}
        req = requests.post(url=self.kakao_url, data=data, headers=self.headers)

        if req.status_code != 200:
            raise SocialLoginFailException

        access_token = req.text.encode('utf8')
        if not access_token:
            raise SocialLoginFailException
        return True

    async def _register_by_facebook(self, dto: CreateUserDto) -> bool:
        # TODO: 소셜 로그인 연동 필요
        data = {'email': dto.email, 'password': dto.password1}
        req = requests.post(url=self.facebook_url, data=data, headers=self.headers)

        if req.status_code != 200:
            raise SocialLoginFailException

        access_token = req.text.encode('utf8')
        if not access_token:
            raise SocialLoginFailException
        return True

    async def _register_by_default(self, dto: CreateUserDto):
        pass
