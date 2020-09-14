import requests

class Requests:
    def request(self, url, method, **kwargs):
        return requests.request(url=url, method= method, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url= url, method= 'get', **kwargs)
    def post(self, url, **kwargs):
        return self.request(url= url, method= 'post', **kwargs)
    def put(self, url, **kwargs):
        return self.request(url= url, method= 'put', **kwargs)
    def delete(self, url, **kwargs):
        return self.request(url= url, method= 'delete', **kwargs)