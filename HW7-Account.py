#Account Assignment
#Weiwei Su
#U17420699
#Last Date Modified: 11/25/2017

import pickle
import tempfile
import os

#Transaction Class
class Transaction:
    def __init__(self, amount, date, currency = "USD", conversionRate = 1.0, description = None): #Default Rate is 1
        #use __ as private attribute.
        self.__amount = amount
        self.__date = date #Format of Date is YYYY-MM-DD
        self.__currency = currency
        self.__conversionRate = conversionRate
        self.__description = description
        self.__usd = amount * conversionRate

    def getAmount(self):
        return self.__amount

    def getDate(self):
        return self.__date

    def getCurrency(self):
        return self.__currency

    def getRate(self):
        return self.__conversionRate

    def getDescription(self):
        return self.__description

    def getUsd(self):
        return self.__usd

    def __str__(self):
        return "%f %s %s %f %s" %(self.getAmount(), self.getDate(), self.getCurrency(), self.getRate(), self.getDescription())

#Account Class
class Account:
    def __init__(self, number, name, transacationList):
        self.__accountNumber = number
        assert len(name) >= 4 #At least 4 chars long
        self.__accountName = name
        self.__transacationList = transacationList
        self.__balance = 0.0
        self.__all_usd = True
        for t in transacationList:
            self.__balance  += t.getUsd()
        for t in transacationList:
            if t.getCurrency() != "USD":
                self.__all_usd = False
                break

    def getAccountNumber(self):
        return self.__accountNumber

    def setAccountName(self, name):
        assert len(name) >= 4
        self.__accountName = name

    def getAccountName(self):
        return self.__accountName

    def getBalance(self):
        return self.__balance

    def getAllUsd(self):
        return self.__all_usd

    def apply(self, transaction):
        self.__transacationList.append(transaction)
        self.__balance += transaction.getUsd()
        if transaction.getCurrency() != "USD":
            self.__all_usd = False
#Load infor from .acc
    def load(self, filename = ""):
        if filename == "":
            filename = "%d.acc" % (self.__accountNumber)
        try:
            fh = open(filename, "rb")
            data = pickle.load(fh)
            all_data = data.strip().split("\n")
            self.__accountNumber = int(all_data[0])
            self.__accountName = all_data[1]
            self.__transacationList = []
            for d in all_data[2:]:
                item = d.strip().split()
                amount = float(item[0])
                date = item[1]
                currency = item[2]
                usd_conversion_rate = float(item[3])
                description = None
                if len(item) >= 5:
                    description = item[4]
                self.__transacationList.append(Transaction(amount, date, currency, usd_conversion_rate, description))


        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise pickle.PickleError(str(err))
        finally:
            if fh is not None:
                fh.close()
#Save File to .acc format
    def save(self, filename = ""):
        if filename == "":
            filename = "%d.acc" % (self.__accountNumber)
        try:
            data = str(self.__accountNumber) + "\n" + str(self.__accountName) + "\n"
            for t in self.__transacationList:
                data += str(t)
                data += "\n"
            fh = open(filename, "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise pickle.PickleError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def __len__(self):
        return len(self.__transacationList)
#DOCTEST
if __name__ == "__main__":
    import doctest
    doctest.testmod()