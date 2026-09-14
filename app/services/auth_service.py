from app.core.exceptions import AuthenticationError, DuplicateError
from app.core.security import hash_password, verify_password
from app.models import Role, User
from app.repositories import UserRepository
from app.utils import log_call


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.current_user: User | None = None

    @log_call
    def register(
        self,
        username: str,
        password: str,
        /,
        *,
        role: Role = Role.USER,
    ) -> User:
        """Username is positional-only; role is keyword-only."""
        username = username.strip()
        if not username or len(password) < 8:
            raise ValueError("Username is required and password must be at least 8 chars")
        if self.user_repository.get_by_username(username):
            raise DuplicateError("Username already exists")
        user = User(username, hash_password(password), role)
        return self.user_repository.save(user)

    def login(self, username: str, password: str) -> User:
        user = self.user_repository.get_by_username(username.strip())
        if user is None or not verify_password(password, user.password_hash):
            raise AuthenticationError("Invalid username or password")
        self.current_user = user
        return user

    def logout(self) -> None:
        self.current_user = None
from app.core.exceptions import AuthenticationError, DuplicateError
from app.core.security import hash_password, verify_password
from app.models import Role, User
from app.repositories import UserRepository
from app.utils import log_call


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.current_user: User | None = None

    @log_call
    def register(
        self,
        username: str,
        password: str,
        /,
        *,
        role: Role = Role.TEACHER,
    ) -> User:
        """Username is positional-only; role is keyword-only."""
        username = username.strip()
        if not username or len(password) < 8:
            raise ValueError("Username is required and password must be at least 8 chars")
        if self.user_repository.get_by_username(username):
            raise DuplicateError("Username already exists")
        user = User(username, hash_password(password), role)
        return self.user_repository.save(user)

    def login(self, username: str, password: str) -> User:
        user = self.user_repository.get_by_username(username.strip())
        if user is None or not verify_password(password, user.password_hash):
            raise AuthenticationError("Invalid username or password")
        self.current_user = user
        return user

    def logout(self) -> None:
        self.current_user = None
