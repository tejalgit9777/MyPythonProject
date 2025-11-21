# Encapsulation of API Token with Inheritance

class BaseAPI:
    __token = "ABC123SECRET"

    def _gettoken(self):
        return self.__token

class UserAPI(BaseAPI):

    def get_user_data(self):
        print("Fetching user data using token: ", self._gettoken())

user_API = UserAPI()
user_API.get_user_data()



