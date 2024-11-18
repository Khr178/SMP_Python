#приховує логіку отримання даних через API
#відповідає за те, щоб отримати дані (користувачів або їх пости) від UserAPIConnector.
class UserRepository:
    def __init__(self, api_connector):
        self.api_connector = api_connector

    def get_all_users(self):
        return self.api_connector.get_users()

    def get_user_posts(self, user_id):
        return self.api_connector.get_user_posts(user_id)

    def get_user_by_name(self, name):
        users = self.api_connector.get_users()
        for user in users:
            if user['name'].lower() == name.lower():
                return user
        return None



