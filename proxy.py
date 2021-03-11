class Proxy:
    def __init__(self,proxy):
        pro = proxy.split(":")
        self.username = pro[2]
        self.password = pro[3]
        self.host = pro[0]
        self.port = pro[1]
        return 

    def geUsername(self):
        return self.username
    def gePassword(self):
        return self.password
    def getHost(self):
        return self.host
    def gePort(self):
        return self.port
    def getProxy(self):
        return f"{self.username}:{self.password}@{self.host}:{self.port}"
    def __str__(self):
        return f"{self.username}:{self.password}@{self.host}:{self.port}"