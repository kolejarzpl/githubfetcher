# w plikach typu service, przechowuje sie metody ktore maja za zadanie np pobrac jakies dane z repo, wykonac jakas logike i zwrocic odpowiednio przetworzone dane
from repository import userRepository


def add_users(payload):
    print("Adding new users")
    userRepository.save_users(payload)


def get_all_users():
    print(f"Getting all users")
    return userRepository.get_all_users()


def get_user_by_name(name):
    print("Getting user with name: " + name)
    return userRepository.get_user_by_name(name)
