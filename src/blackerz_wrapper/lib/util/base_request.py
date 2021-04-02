import requests, time
from threading import Thread

superagent = "Blackerz 1.0"
default_baseURL = "https://blackerz.herokuapp.com"

class request():
    def __init__(self, url="", data=None, timeout=30, headers=None, cookies=None, json=None):
        self.super_agent = superagent
        self.url = url
        self.data = data
        self.json = json
        self.timeout = timeout
        self.headers = headers or {}
        self.cookies = cookies
        self.headers["user-agent"] = self.super_agent

    def get(self):
        return requests.get(url=self.url, timeout=self.timeout, headers=self.headers, cookies=self.cookies)

    def post(self):
        return requests.post(url=self.url, data=self.data, json=self.json, timeout=self.timeout, headers=self.headers, cookies=self.cookies)

    def put(self):
        return requests.put(url=self.url, data=self.data, json=self.json, timeout=self.timeout, headers=self.headers, cookies=self.cookies)    


class loopThread(Thread):
    def __init__(self, functi, interval=1, args=[]):
        Thread.__init__(self)
        self.daemon = True
        self.function = functi
        self.interval = interval
        self.args = args
        self.start()
    def run(self):
        while True:
            self.function(*self.args)
            time.sleep(self.interval)