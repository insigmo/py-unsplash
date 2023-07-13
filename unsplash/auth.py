from typing import Optional

from oauthlib.oauth2 import OAuth2Error
from requests_oauthlib.oauth2_session import OAuth2Session
from unsplash.errors import UnsplashAuthError


class Auth:
    DEFAULT_VERSION = "v1"
    BASE_API_URL = "https://api.unsplash.com"
    BASE_AUTH_URL = "https://unsplash.com"

    def __init__(
            self,
            client_id: str,
            client_secret: str,
            redirect_uri: str,
            token: Optional[dict] = None,
            code: Optional[str] = None,
            scope: Optional[str] = None
    ):
        self.access_token_url = "%s/oauth/token" % self.BASE_AUTH_URL
        self.authorization_url = "%s/oauth/authorize" % self.BASE_AUTH_URL
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token: Optional[dict] = None
        self.access_token: Optional[str] = None
        self.is_authenticated = False
        self.scope_list = [
            "public",
            "read_user",
            "write_user",
            "read_photos",
            "write_photos",
            "write_likes",
            "write_followers",
            "read_collections",
            "write_collections"
        ]
        self.scope = scope or self.scope_list

        try:
            if token:
                self.oauth = OAuth2Session(
                    client_id=self.client_id, redirect_uri=self.redirect_uri, scope=self.scope, token=token
                )
                self.access_token = self.oauth.access_token
                self.token = token
                self.is_authenticated = True
            elif code:
                self.oauth = OAuth2Session(client_id=self.client_id, redirect_uri=self.redirect_uri, scope=self.scope)
                self.access_token = self.get_access_token(code)
                self.is_authenticated = True
        except OAuth2Error as e:
            raise UnsplashAuthError(e)

    def get_access_token(self, code: str) -> dict:
        self.token = self.oauth.fetch_token(
            token_url=self.access_token_url,
            client_id=self.client_id,
            client_secret=self.client_secret,
            scope=self.scope,
            code=code
        )
        return self.token.get("access_token")

    def get_refresh_token(self):
        return self.token.get("refresh_token")

    def refresh_token(self):
        self.token = self.oauth.refresh_token(self.access_token_url, refresh_token=self.get_refresh_token())
        self.access_token = self.token.get("access_token")
