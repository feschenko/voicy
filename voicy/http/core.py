import requests


class Request:
    def __init__(self, session: requests.Session = None):
        self.session = session or requests.session()

    def make(
        self,
        method: str,
        url: str,
        data: dict = None,
        params: dict = None,
        json: dict = None,
        headers: dict = None,
    ) -> requests.Response:
        if self.session:
            return self.session.request(
                method=method,
                url=url,
                data=data,
                params=params,
                json=json,
                headers=headers,
            )
        else:
            return requests.request(
                method=method,
                url=url,
                data=data,
                params=params,
                json=json,
                headers=headers,
            )
