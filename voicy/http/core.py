import requests


class Request:
    @staticmethod
    def make(
        method: str,
        url: str,
        data: dict = None,
        params: dict = None,
        json: dict = None,
        headers: dict = None,
    ) -> requests.Response:
        return requests.request(
            method=method, url=url, data=data, params=params, json=json
        )
