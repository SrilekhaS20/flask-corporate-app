from app.models.user import User

class UserService:
    @staticmethod
    def get_user():
        return User(1, "Sri", "sri@example.com")