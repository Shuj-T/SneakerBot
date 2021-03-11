from shoeBot import ShoeBot
from account import Account
from proxy import Proxy
import threading,time

from fileReaders import getAccounts,getProxies
from display import divider,title
from display import divider,title,bcolors
class Manager():
    proxies = []
    accounts = []
    #def ___innit__(self,botNum,):


def menu():
    getAccounts()
    print(f"{bcolors.HEADER}{title}{bcolors.ENDC}")
    searchType = input(f"""{bcolors.OKGREEN}Search Link or Shoe Name:{bcolors.ENDC}{bcolors.OKBLUE}
    1.Link (recommended)
    2.Shoe Name{bcolors.ENDC}
--------------------------------
""")
    if searchType == "test":
        print("Fast Mode")
    elif searchType == "x":
        print("Bye!")
    else:
        website = input(f"""
--------------------------------
{bcolors.OKGREEN}Which Website would you like to Cope from:{bcolors.ENDC}{bcolors.OKBLUE}
    1.FootLocker{bcolors.ENDC}
--------------------------------
""")
        if searchType == "1":
            shoeLink = input(f"""{divider}{bcolors.OKGREEN}Enter The Link Of The Shoe:{bcolors.ENDC}{divider}""")
        if searchType == "2":
            shoeName = input(f"""{divider}{bcolors.OKGREEN}Enter The Name Of The Shoe:{bcolors.ENDC}{divider}""")
        shoeSizes = input(f"""{divider}{bcolors.OKGREEN}Enter The Shoes size (seperated by commas in the order you want them):{bcolors.ENDC}\n e.g 6,8,7{divider}""")
        shoeSizes = shoeSizes.split(",")
        botNum =  input(f"""{divider}{bcolors.OKGREEN}Enter The Number of  bots you want to run:{bcolors.ENDC}{divider}""")
    print(f"ShoeLink:{shoeLink}")
    print(f"ShoeSizes:{shoeSizes}")
    return (shoeLink,shoeSizes,botNum)

if __name__ == "__main__":
    shoeName = None
    accounts = getAccounts()
    proxies = getProxies()
    
    for account in accounts:
        print(account)
    for proxy in proxies:
        print(proxy)
    confirm = input(f"{bcolors.FAIL}WARING! Please confirm the ABOVE information is correct before proceeding (Y/N):{bcolors.ENDC}{divider}")
    if confirm == "y" or confirm == "Y":
        link,sizes,botNum = menu()
        accMax =int(botNum)/len(accounts)
        accNum = 0
        j = 0
        thread_list = list()
        print ("Creating Bots!")
        for i in range(int(botNum)):
            if j >= accMax:
                accNum+=1
            t = threading.Thread(name='Bot {}'.format(i), target=ShoeBot, args=(link,sizes,accounts[accNum]))
            t.start()
            print (t.name + ' started!')
            thread_list.append(t)
            j += 1
        for thread in thread_list:
            thread.join()
        print ("Bots Done!")

    else:
        print("Correct the information and come back!")
