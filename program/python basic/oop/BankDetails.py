class BankDetails:
    def __init__(self,custid, cname, bal):
        self._custid = custid
        self._cname = cname
        self._bal = bal
    def welcome_message(self):
        print("Welcome to SBI ")
    def display_details(self):
        print(f'{self._custid}-{self._cname}-{self._bal}')
