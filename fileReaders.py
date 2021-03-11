from account import Account
from proxy import Proxy
def getAccounts():
    with open('accounts.txt') as accounts:
        accountObj = []
        accounts = [line.rstrip('\n') for line in accounts]
        for account in accounts:
            det = account.split(",")
            accountObj.append(Account(det[0],det[1],det[2],det[3],det[4],det[5],det[6]))
    return accountObj
    
def getProxies():
    with open('proxies.txt') as proxies:
        proxyobj = []
        proxies = [line.rstrip('\n') for line in proxies]
        for proxy in proxies:
            proxyobj.append(Proxy(proxy))
    return proxyobj