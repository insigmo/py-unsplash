from unsplash.collection import Collection
from unsplash.photo import Photo
from unsplash.search import Search
from unsplash.stat import Stat
from unsplash.user import User


class Api:
    def __init__(self, auth, api_version=None):
        self._auth = auth
        self.base_url = self._auth.BASE_API_URL
        self.base_auth_url = self._auth.BASE_AUTH_URL
        self.api_version = api_version or self._auth.DEFAULT_VERSION
        self.client_id = self._auth.client_id

    @property
    def access_token(self):
        return self._auth.access_token

    @property
    def is_authenticated(self):
        return self._auth.is_authenticated

    @property
    def photo(self) -> Photo:
        return Photo(api=self)

    @property
    def user(self) -> User:
        return User(api=self)

    @property
    def search(self) -> Search:
        return Search(api=self)

    @property
    def collection(self) -> Collection:
        return Collection(api=self)

    @property
    def stat(self) -> Stat:
        return Stat(api=self)
