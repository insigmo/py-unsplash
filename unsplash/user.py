from unsplash.client import Client
from unsplash.models import Collection as CollectionModel
from unsplash.models import Link as LinkModel
from unsplash.models import Photo as PhotoModel
from unsplash.models import User as UserModel


class User(Client):
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.ordering_values = ["latest", "oldest", "popular"]

    def me(self):
        url = "/me"
        result = self._get(url)
        return UserModel.parse(result)

    def update(self, **kwargs):
        url = "/me"
        result = self._put(url, data=kwargs)
        return UserModel.parse(result)

    def get(self, username, width=None, height=None):
        url = "/users/{username}".format(username=username)
        params = {
            "w": width,
            "h": height
        }
        result = self._get(url, params=params)
        return UserModel.parse(result)

    def portfolio(self, username: str):
        url = "/users/{username}/portfolio".format(username=username)
        result = self._get(url)
        return LinkModel.parse(result)

    def _photos(self, url, page: int = 1, per_page: int = 10, order_by: str = "latest"):
        if order_by not in self.ordering_values:
            raise Exception()
        params = {
            "page": page,
            "per_page": per_page,
            "order_by": order_by
        }
        return self._get(url, params=params)

    def photos(self, username, page: int = 1, per_page: int = 10, order_by: str = "latest"):
        url = "/users/{username}/photos".format(username=username)
        result = self._photos(url, page=page, per_page=per_page, order_by=order_by)
        return PhotoModel.parse_list(result)

    def likes(self, username, page: int = 1, per_page: int = 10, order_by: str = "latest"):
        url = "/users/{username}/likes".format(username=username)
        result = self._photos(url, page=page, per_page=per_page, order_by=order_by)
        return PhotoModel.parse_list(result)

    def collections(self, username, page: int = 1, per_page: int = 10):
        url = "/users/{username}/collections".format(username=username)
        params = {
            "page": page,
            "per_page": per_page
        }
        result = self._get(url, params=params)
        return CollectionModel.parse_list(result)
