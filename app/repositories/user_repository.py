from app.core.config import settings
from app.models import User
from app.repositories.json_repository import JsonRepository


class UserRepository:
    def __init__(self):
        self._repo = JsonRepository[User](settings.data_file, "users")

    def list(self) -> list[User]:
        return [User.from_dict(item) for item in self._repo.list()]

    def get_by_username(self, username: str) -> User | None:
        return next((u for u in self.list() if u.username == username), None)

    def save(self, user: User) -> User:
        items = [u for u in self.list() if u.id != user.id]
        items.append(user)
        self._repo.replace_all([u.to_dict() for u in items])
        return user
