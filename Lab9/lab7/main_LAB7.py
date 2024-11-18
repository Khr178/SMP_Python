from UI.user_interface_LAB7 import UserInterface
from service_factory_LAB7 import ServiceFactory

def run():
    ui = UserInterface()
    ui.menu()
    user_interface = ServiceFactory.create_user_interface()
    user_interface.menu()

if __name__ == "__main__":
    run()
