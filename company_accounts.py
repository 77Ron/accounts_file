#Company accounts

from company_info import *

class Account:

    company = company_name
    
    def __init__(self, dept = 0, name= "-None-", id = 0, address = "-Blank-", p_code = "--- ---", balance = 0.00):
        self.dept = dept
        self.name = name
        self.id = id
        self.address = address
        self.p_code = p_code
        self.balance = balance
   
    def __str__(self):
        return "Company: %s   %i %-15s  %-20s   %i  %s, %s, %.2f %.2f"\
              % (self.company, self.dept, self.deptname, self.name, self.id, self.address, self.p_code, self.balance, self.discnt)
    
class Dept1Account(Account):

    def __init__(self, dept = 1, name= "-None-", id = 0, address = "-Blank-", p_code = "--- ---", balance = 0.00):
        Account.__init__(self, dept, name, id, address, p_code, balance)
        self.deptname = dept1
        self.discnt = self.discount()

    def discount(self):
        disc1 = round(d1dc1/100, 2)
        if self.balance < 0:
            disc1 = 0
        if self.balance > d1rng:
            disc1 = round(d1dc2/100, 2)
        return round(self.balance * disc1, 2)

class Dept2Account(Account):

    def __init__(self, dept = 2, name= "-None-", id = 0, address = "-Blank-", p_code = "--- ---", balance = 0.00):
        Account.__init__(self, dept, name, id, address, p_code, balance)
        self.deptname = dept2
        self.discnt = self.discount()
    
    def discount(self):
        disc2 = round(d2dc1/100, 2)
        if self.balance < 0:
            disc2 = 0
        if self.balance > d2rng:
            disc2 = round(d2dc2/100, 2)
        return round(self.balance * disc2, 2)

class Dept3Account(Account):

    def __init__(self, dept = 3, name= "-None-", id = 0, address = "-Blank-", p_code = "--- ---", balance = 0.00):
        Account.__init__(self, dept, name, id, address, p_code, balance)
        self.deptname = dept3
        self.discnt = self.discount()

    def discount(self):
        disc3 = round(d3dc1/100, 2)
        if self.balance < 0:
            disc3 = 0
        if self.balance > d3rng:
            disc3 = round(d3dc2/100, 2)
        return round(self.balance * disc3, 2)