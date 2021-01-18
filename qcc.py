import requests
from json.decoder import JSONDecodeError


class ResultError(ValueError):
    def __init__(self, url, result):
        self.result = result
        errmsg = '请求 %s: 返回的结果不是JSON格式，请检查企查查账户是否有访问权限或检查Cookies是否过期。以下为返回结果仅供调试：\n %s' % (url, result)
        ValueError.__init__(self, errmsg)
        self.msg = url

    def __reduce__(self):
        return self.__class__, (self.msg, self.result)


class QccWebApi:

    def __init__(self, cookies) -> object:
        self.base_path = "https://www.qcc.com/api/"
        self.headers = {
            "referer": "https://www.qcc.com/web/charts/find-relation",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66",
            "x-requested-with": "XMLHttpRequest",
            "sec-fetch-site": "same-origin",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br"
        }
        self.cookies = cookies
        self.headers['cookie'] = self.cookies

    def search_mind(self, search_key: str, page_size: int = 5):
        return self._get(self.get_api_url("search/searchMind"), {"searchKey": search_key, "pageSize": page_size})

    def get_detail(self, key_no: str):
        return self._post(self.get_api_url("charts/getDetail"), {"keyNo": key_no})

    def find_relationship(self, rels: list, nodes: list):
        rels = ",".join(rel for rel in rels)
        nodes = ",".join(node for node in nodes)
        return self._post(self.get_api_url("charts/findRelationships"), {"rels": rels, "nodes": nodes})

    def get_api_url(self, path):
        return self.base_path + path

    def _get(self, url: str, params: dict):
        result = None
        try:
            result = requests.get(url, headers=self.headers, params=params)
            result = result.json()
        except JSONDecodeError as jed:
            raise ResultError(url, result.content)
        return result

    def _post(self, url: str, data: dict):
        result = None
        try:
            result = requests.post(url, headers=self.headers, data=data)
            result = result.json()
        except JSONDecodeError as jed:
            raise ResultError(url, result.content)
        return result
