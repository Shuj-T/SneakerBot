class Account:
    trace = True
    def __init__(self,email,password,cardNumber,cardName,cvcCode,exYear,exMonth):
        test = False
        if (self.trace or test):
            print("Account:__init__:START")
        self.email = email
        self.password = password
        self.cardNumber = cardNumber
        self.cardName = cardName
        self.cvcCode = cvcCode
        self.exYear = exYear
        self.exMonth = exMonth
        if (self.trace or test):
            print("Account:__init__:END")
    def __str__(self):
        return (f"""Email: {self.email}
Password: {self.password}
CardNumber: {self.cardNumber}
cvcCode: {self.cvcCode}
ExpiryDate: {self.exMonth}/{self.exYear}
        """)

    def getEmail(self):
        return self.email
    def getPass(self):
        return self.password
    def getCardNumber(self):
        return self.cardNumber
    def getCardName(self):
        return self.cardNumber
    def getCVC(self):
        return self.cvcCode
    def getYear(self):
        return self.exYear
    def getMonth(self):
        return self.exMonth
