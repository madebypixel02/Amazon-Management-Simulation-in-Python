class Package:
    def __init__(self,package_number, deliver_address, postal_code):
        num = str(package_number)
        self.__packnumber = num[0:3]+'-'+num[3:10]+'-'+num[10:]
        self.__address = deliver_address
        self.__postcode = postal_code
        self.__strikes = 3
    # T(n) = 10

    
    def printInfo(self):
        string = ''
        string += 'ID: ' + self.__packnumber
        string +=' Zone: ' + str(self.__postcode)
        return string
    # T(n) = 3 
    
    @property
    def packnumber(self):
        return self.__packnumber
    # T(n) = 1

    
    @property
    def address(self):
        return self.__address
    # T(n) = 1
    
    @property
    def postcode(self):
        return self.__postcode
    # T(n) = 1
    
    @property
    def strikes(self):
        return self.__strikes
    # T(n) = 1
    
    @strikes.setter
    def strikes(self, value):
        self.__strikes = value
    # T(n) = 1