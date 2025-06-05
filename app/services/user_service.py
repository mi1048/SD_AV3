from app.models.user import User

class UserService:
    def __init__(self):
        self.users = []
    
    def create_user(self, user: User):
        self.users.append(user)
        return user
    
    def get_user(self, username: str):
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def update_score(self, username: str, score: int):
        user = self.get_user(username)
        if user:
            user.score = score
            return user
        return None