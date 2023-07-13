from typing import Dict, List, Optional

import requests

from unsplash.errors import UnsplashError


class Client:
    def __init__(self, api, **kwargs):
        self.api = api
        self.rate_limit_error = 'Rate Limit Exceeded'

    def get_auth_header(self) -> Dict[str, str]:
        if self.api.is_authenticated:
            return {"Authorization": "Bearer %s" % self.api.access_token}
        return {"Authorization": "Client-ID %s" % self.api.client_id}

    def get_version_header(self) -> Dict[str, str]:
        return {"Accept-Version": self.api.api_version}

    def _get(self, url, params=None, **kwargs):
        return self._request(url, "get", params=params, **kwargs)

    def _post(self, url, data=None, **kwargs):
        return self._request(url, "post", data=data, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request(url, "delete", **kwargs)

    def _put(self, url, data=None, **kwargs):
        return self._request(url, "put", data=data, **kwargs)

    def _request(self, url: str, method: str, params: Optional[List[str]] = None, data=None, **kwargs):
        url = "%s%s" % (self.api.base_url, url)
        headers = self.get_auth_header()
        headers.update(self.get_version_header())
        headers.update(kwargs.pop("headers", {}))

        try:
            response = requests.request(method, url, params=params, data=data, headers=headers, **kwargs)
        except Exception as e:
            raise UnsplashError("Connection error: %s" % e)

        try:
            response.raise_for_status()
            return response.json()

        except ValueError as e:
            return
