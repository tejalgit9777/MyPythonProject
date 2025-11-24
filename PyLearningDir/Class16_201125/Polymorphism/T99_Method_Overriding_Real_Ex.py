# real example

class Request:

    def make_http_request(self, url):
        print("Lets make the HTTP request without auth", url)

    def make_http_request(self, url, auth=None):
        print("Lets make the HTTP request with auth", url,auth)

req = Request()
req.make_http_request(url="http://www.python.org")
