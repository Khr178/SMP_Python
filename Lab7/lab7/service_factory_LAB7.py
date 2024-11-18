from DAL.user_api_connector_LAB7 import UserAPIConnector
from BLL.user_repository_LAB7 import UserRepository
from UI.user_interface_LAB7 import UserInterface

#дозволяє передавати об’єктам (класам) їх залежності ззовні замість того, щоб класи самі створювали ці залежності.
class ServiceFactory:
    @staticmethod
    def create_user_interface():
        api_connector = UserAPIConnector()  # створ як Залежність для UserRepository
        user_repository = UserRepository(api_connector)  # Залежність для UserInterface
        return UserInterface(user_repository)  # передача залежності у UserInterface
