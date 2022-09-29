class payrolldeduction:
    def __init__(self, description, date, chargeamount, employeeid):
        self._description=description
        self._date=date
        self._chargeamount=chargeamount
        self._employeeid=employeeid
    
    def set_description(self, description):
        self._description=description

    def set_date(self, date):
        self._date=date

    def set_chargeamount(self, chargeamount):
        self._chargeamount=chargeamount

    def set_employeeid(self, employeeid):
        self._employeeid=employeeid
    
    def get_description(self):
        return self._description

    def get_date(self):
        return self._date
    
    def get_chargeamount(self):
        return self._chargeamount

    def get_employeeid(self):
        return self._employeeid

