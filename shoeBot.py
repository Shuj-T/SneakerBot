from account import Account
from fileReaders import getAccounts, getProxies
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import re
#from .shoeManager import bcolors
import time 
PATH = "C:\Program Files (x86)\chromedriver.exe"
class ShoeBot:
    trace = True
    #This is if we have the shoe link
    def __init__(self,link,sizes,account,proxy = None):
        test = False
        if (self.trace or test):
            print("ShoeBot:__init__:START")
        vars(self)['status'] = "Preparing..."
        self.link = link
        self.sizes = sizes
        self.account = account
        self.proxy = proxy
        self.openSite(False,self.proxy)
        aval = self.availableSizes()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        for size in self.sizes:
            print(f"s:{size},a:{aval}")
            if size in aval:
                self.getShoe(aval[size])
                break
        #time.sleep(10)
        # recap = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_elements_located(("//*[contains(text(),'I'm not a robot')]")))
        #recap = self.driver.findElements(By.xpath("//*[contains(text(),'I'm not a robot')]"));

        src = self.driver.page_source
        recap = re.search(r'We want to make sure it is actually you we are dealing with and not a robot.', src)
        if recap != None:
            print("Opps! RECAPTCHA!")
        elif recap == None:
            print("NO RECAPTCHA!")
            
        # try:
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located(("//*[contains(text(),'I'm not a robot')]"))
        #     )
        #WebElement m = driver.findElement (By.xpath ("//*[contains(text(),'I'm not a robot')]"));
        # except TypeError:
        #     print("There is a CAPTCHA")
        # finally:
        #     print("Awsome")
        # recap = self.driver.find_element_by_xpath("""//*[@id="captcha-container"]""")
        # if recap != None:
        #     print("Opps! RECAPTCHA!")
        self.checkout()
            
        if (self.trace or test):
            print("ShoeBot:__init__:END")
        return

    def __setattr__(self, attr, value):
        if attr == 'status':
            print('{}'.format(value))
        super().__setattr__(attr, value)
    
    def openSite(self,headless = None,proxy = None):
        vars(self)['status'] = "Opening Website..."
        chrome_options = webdriver.ChromeOptions()
        chrome_options = Options()
        if headless == True:
            chrome_options.add_argument("--headless")
        if proxy != None: 
            proxy = self.proxy.getProxy()
            chrome_options.add_argument('--proxy-server=%s' %proxy)
        self.driver = webdriver.Chrome(PATH,options=chrome_options)
        self.driver.set_window_size(2000 , 2000)
        self.driver.get(self.link)
        try:
            vars(self)['status'] = "Wating in queue..."
            element = WebDriverWait(self.driver, 18000).until(
            EC.presence_of_element_located((By.XPATH, """//*[@id="fitanalytics_sizecontainer"]/section[3]/div/button"""))
        )
        finally:
            print("")
        vars(self)['status'] = "On Item Page"
        return

    def availableSizes(self):
    
        test = False
        if (self.trace or test):
            print("ShoeBot:availableSizes:START")

        vars(self)['status'] = "Checking Sizes..."
        available = {}
        i = 1
        sizes = self.driver.find_elements_by_xpath("""//*[@id="fitanalytics_sizecontainer"]/section[3]/div/button""")
        for size in sizes:
            if (size.get_attribute("class") != "fl-product-size--item fl-product-size--item__not-available"):
                if (self.trace or test):
                    print(f"""Size:{size.text},Availability:{size.get_attribute("class")}""")
                available[size.text]=i
                i += 1

        if (self.trace or test):
            print("ShoeBot:availableSizes:END")
        return available
    
    def getShoe(self,position):
        test = False
        if (self.trace or test):
            print("ShoeBot:getShoe:START")
        
        vars(self)['status'] = "Adding Shoe to cart..."
        #size = self.driver.find_element_by_xpath(f"""//*[@id="fitanalytics_sizecontainer"]/section[3]/div/button[{position}]""")
        # print(position)
        # xxx = f"//section[3]/div/button[{position}]"
        # print(xxx)
        shoeSize = self.driver.find_element(By.XPATH, f"//section[3]/div/button[{position}]")
        shoeSize.click()
        addToCart = self.driver.find_element(By.XPATH, "//span[contains(.,\'ADD TO CART\')]")
        addToCart.click()
        if (self.trace or test):
            print("ShoeBot:getShoe:END")
        return
    def checkout(self):
        test = False
        if (self.trace or test):
            print("ShoeBot:checkout:START")
        self.account
        email = self.account.getEmail()
        password = self.account.getPass()
        cardNumber = self.account.getCardNumber()
        cardName = self.account.getCardName()
        cvcCode = self.account.getCVC()
        exYear = self.account.getYear()
        exMonth = self.account.getMonth()
        try:
            print("Please Check if this is a RECAPTCHA!")
            start = time.perf_counter()
            element = WebDriverWait(self.driver, 1000000000000000000000000000).until(
                EC.presence_of_element_located((By.XPATH, "//div[7]/div/a/span"))
            )
            end = time.perf_counter()
        finally:
            vars(self)['status'] = "Checking out ..."
            self.driver.find_element(By.XPATH, "//div[7]/div/a/span").click()
            self.driver.find_element(By.ID, "fl-login-input-email-checkout-split-login-panel").click()
            self.driver.find_element(By.ID, "fl-login-input-email-checkout-split-login-panel").click()
            self.driver.find_element(By.ID, "fl-login-input-email-checkout-split-login-panel").send_keys(email)
            self.driver.find_element(By.ID, "fl-input-password-checkout-split-login-panel").click()
            self.driver.find_element(By.ID, "fl-input-password-checkout-split-login-panel").send_keys(password)
            self.driver.find_element(By.CSS_SELECTOR, ".col-sm-8 .fl-btn--inner").click()
            self.driver.find_element(By.CSS_SELECTOR, ".radio:nth-child(1) strong").click()
            self.driver.find_element(By.CSS_SELECTOR, ".payment-name").click()
            self.driver.find_element(By.CSS_SELECTOR, ".fl-label--inner > .fl-comp-html").click()
            self.driver.find_element(By.CSS_SELECTOR, ".fl-btn__primary > .fl-btn--inner").click()
            self.driver.find_element(By.CSS_SELECTOR, ".pmBcard").click()
            self.driver.find_element(By.ID, "card.cardNumber").click()
            self.driver.find_element(By.ID, "card.cardNumber").click()
            self.driver.find_element(By.ID, "card.cardNumber").send_keys(cardNumber)
            self.driver.find_element(By.ID, "card.cardHolderName").click()
            self.driver.find_element(By.ID, "card.cardHolderName").click()
            self.driver.find_element(By.ID, "card.cardHolderName").send_keys(cardName)
            self.driver.find_element(By.ID, "card.expiryMonth").click()
            dropdown = self.driver.find_element(By.ID, "card.expiryMonth")
            dropdown.find_element(By.XPATH, f"//option[. = '{exMonth}']").click()
            self.driver.find_element(By.ID, "card.expiryMonth").click()
            self.driver.find_element(By.ID, "card.expiryYear").click()
            dropdown = self.driver.find_element(By.ID, "card.expiryYear")
            dropdown.find_element(By.XPATH, f"//option[. = '{exYear}']").click()
            self.driver.find_element(By.ID, "card.expiryYear").click()
            self.driver.find_element(By.ID, "card.cvcCode").click()
            self.driver.find_element(By.ID, "card.cvcCode").send_keys(cvcCode)
            self.driver.find_element(By.ID, "pmmdetails-card").click()
            self.driver.find_element(By.CSS_SELECTOR, ".paySubmitcard").click()
            self.driver.find_element(By.CSS_SELECTOR, "html").click()
            vars(self)['status'] = "Check Out"

        if (self.trace or test):
            print("ShoeBot:checkout:END")
        return

        # def findShoe(shoe):
        #     test = False
        #     if (self.trace or test):
        #         print("ShoeBot:__init__:START")

        #     if (site == "FootLocker"):
        #         search = driver.find_element_by_id("searchTerHeader")
        #         time.sleep(1)
        #         search.send_keys(shoe)
        #         search.send_keys(Keys.RETURN)

        #     if (self.trace or test):
        #         print("ShoeBot:__init__:END") 
def __test():
    link = "https://www.footlocker.co.uk/en/p/nike-air-more-uptempo-men-shoes-8114?v=314105853304&utm_source=pla&utm_medium=cpc&utm_campaign=10933359828&utm_content=112771687372_459141047219&_cclid=Google_EAIaIQobChMI_LqO36Pq7gIVRbTtCh0KUQmPEAQYASABEgJHyPD_BwE&gclid=EAIaIQobChMI_LqO36Pq7gIVRbTtCh0KUQmPEAQYASABEgJHyPD_BwE"
    sizes = ["8"]
    account = getAccounts()[0]
    bot = ShoeBot(link,sizes,account)
if __name__ == "__main__":
    __test()
