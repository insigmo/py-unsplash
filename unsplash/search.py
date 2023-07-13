from unsplash.client import Client
from unsplash.models import Collection as CollectionModel
from unsplash.models import Photo as PhotoModel
from unsplash.models import User as UserModel


class Search(Client):
    def __init__(self, **kwargs):
        super(Search, self).__init__(**kwargs)

    def _search(self, url, query, page: int = 1, per_page: int = 10):
        params = {
            "query": query,
            "page": page,
            "per_page": per_page
        }
        return self._get(url, params=params)

    def photos(self, query, page: int = 1, per_page: int = 10):
        url = "/search/photos"
        data = self._search(url, query, page=page, per_page=per_page)
        data["results"] = PhotoModel.parse_list(data.get("results"))
        return data

    def collections(self, query, page: int = 1, per_page: int = 10):
        url = "/search/collections"
        data = self._search(url, query, page=page, per_page=per_page)
        data["results"] = CollectionModel.parse_list(data.get("results"))
        return data

    def users(self, query, page: int = 1, per_page: int = 10):
        url = "/search/users"
        data = self._search(url, query, page=page, per_page=per_page)
        data["results"] = UserModel.parse_list(data.get("results"))
        return data
