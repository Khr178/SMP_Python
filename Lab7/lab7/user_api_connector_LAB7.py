import requests

class UserAPIConnector:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_users(self):
        response = requests.get(f"{self.BASE_URL}/users")
        return response.json()

    def get_user_posts(self, user_id):
        response = requests.get(f"{self.BASE_URL}/posts", params={"userId": user_id})
        return response.json()


