'''
This is an Employee Management system...
Author : Aliasgar Khimani
Date : May 10, 2020
:D
'''

'''The 'Store' class is the Parent class the contains the data and
  methods for the store'''


class Store:
    
    report = open('reports.txt','a+')
    
    
    '''storeList contains a list of all stores registered'''
    storeList = []
    assigned_Budget = dict()
    customer_log = {}
    '''this dictionary comtains the assignment of the budget
    in format : 'assignment' to 'assigned money'''
    prodLis = {}
    
    
    def __init__(self, storeName, storeAddress, netRevenue):
        '''
        The __init__ method contains the basic information like 
        the store's name, address, and total revenue it earns 
        per annum
        '''
        self.storeName = storeName
        self.storeAddress = storeAddress
        self.netRevenue = netRevenue
        
        self.storeList.append(self.storeName)
    
    '''to display the list of all registered stores'''
    def disp_all_stores(self):
            return self.storeList
    
    def assign_Budget(self):
        
        '''
        This method allows the user to access the assigned_Budget list and 
        make it up from scratch
        '''
        
        temp_rev = self.netRevenue
        main_dict = dict()
        
        while temp_rev > 0:
            
            print("Enter name of assignment (Amount Left:{})".format(temp_rev))
            assignment = str(input("Assginment:"))
            amt = int(input("Enter amount to be assigned:"))
            main_dict[assignment] = amt
            temp_rev -= amt
            
            if str(input("Do you wish to contiunue?[y/n]:\nAmount Unassigned:{}".format(temp_rev))) == 'y':continue
            else:break
            
        else:
            
            print("E: No Revenue To Expend")
        
        self.assigned_Budget = main_dict
        print("All done and ready to go :D") 
        
    '''to remove a registered store from list of stores'''
    @classmethod
    def remStore(cls, storeName):
        cls.storeList.pop(storeName)
    
    '''to print out the business card info of the store'''
    @property
    def cardInfo(self):
        return '{}\n{}'.format(self.storeName,self.storeAddress)
    
    @classmethod
    def alterAssignedBudget(cls):
        
        '''
        This is to update exsisting entries of the store's budget
        assignment, if the entry doesn't exist, it is created 
        given that it doesn't surpass the net revenue earned by
        the store
        '''
        
        print("Enter the assignment name you want to alter::")
        print(cls.assigned_Budget)
        alter_this = str(input("Assignment to be altered:"))
        new_val = int(input("Enter new value:"))
    
        try:
            
            cls.assigned_Budget[alter_this] = new_val
            
        except:
            
            print("E:Assignment Not Found")
            print('Creating assignment \'{}\''.format(alter_this))
            cls.assigned_Budget[alter_this] = new_val
    
    @classmethod
    def dBudg(cls):
        
        '''
        This method allows the user to delete an assigned budget
        value...
        '''
        rem_this = str(input("Assignment to be removed:"))
        try:
            del cls.assigned_Budget[rem_this]
        except:
            print("E:Assignment Not Found")
    
    '''
    This method closes the store and deletes the store's 
    name from the list of stores
    '''
    
    @classmethod
    def addProds(cls):
        Store.showProds()
        
        while True:
            
            if str(input("Do you wish to continue[y/n]:")) == 'y':
                continue
            else:
                break
            try:
                prodName = str(input("Enter the name of Product:"))
                prodPrice = float(input('Enter the price of the product:'))
            except:
                pass
            cls.prodLis[prodName] = prodPrice    
    
    @classmethod
    def remProd(cls):
        
        print(cls.showProds())
        
        while True:
            prodName = str(input("Enter the name of the product you want to remove:"))
            
            try:
                del cls.prodLis[prodName]
            except:
                print("E: Please enter a valid product to remove")
            
            if str(input("Do you wish to continue[y/n]:")) == 'y':
                continue
            else:
                break
            
        
    
    def showProds(self):
        print("The Products Currently avaliable are:")
        print('Product Name\t\tProduct Price')
        for i in Store.prodLis:
            try:
                print('\t{}\t|\t{}'.format(i,Store.prodLis[i]))
            except:
                pass
            
    
    @classmethod
    def CloseStoreDown(cls,self):
        auth = str(input("Are you sure you want to Close the store Down?[y/n]:"))
        if auth == 'y':
            cls.storeList.remove(self.storeName)
            del self
        else:
            print("Store Deletion Aborted")
    
        

'''The manager class is for assigning a manager to a store'''      
class Manager(Store):
    
    '''raiseAmt determines by how much will the Manager's salary 
    be raised'''
    raiseAmt = 1.00
    empList = []
    '''this is the list of all the employees working under this manager'''
    
    def __init__(self, name, contact, ID, pay):
        
        super().__init__(storeName = None, storeAddress = None)
        self.name = name
        self.contact = contact
        self.ID = ID
        self.pay = pay
    
    '''method to print out the company email of the manager'''
    @property
    def email(self):
        return '{}@company.com'.format(self.name)
    
    '''prints fullname of the manager'''
    @property
    def fullname(self):
        return '{}'.format(self.name)
    
    '''to change/alter the name of the manager'''
    @fullname.setter
    def fullname(self,name):
        self.name = name
        
    '''to generate all details of the store into a card'''
    def giveCard(self):
        return super.cardInfo()
    
    '''method to raise the pay of the manager'''
    def applyRaise(self):
        self.pay *= raiseAmt
        
    '''displays the list of all current employees under the 
    manager'''
    def disp_Current_Employees(self):
        return self.empList
    
    '''allows manager to register an employee'''
    @classmethod
    def makeEmployee(cls,StoreAs ,name , contact, ID, pay):
        StoreAs = Employee(name,contact,ID,pay)
        cls.empList.append(StoreAs)
    
    '''allows user to change by how much the raise will increase 
    or decrease'''
    @classmethod
    def set_raiseAmount(cls, amount):
        cls.raiseAmt = amount
    
    '''allows manager to fire an employee'''
    @classmethod
    def fireEmployee(cls, empName):
        
        try:
            fire_this_person = str(input("Enter the name of the Employee to be fired:"))
            cls.empList.remove(fire_this_person)
            empName.LeaveJob(empName)
        except:
            print("E: Employee not found")
    
    def EmpLeaves(self, empName):
        self.empList.remove(empName)
    
            

class Employee(Manager):
    
    '''Variable that is accessed when the employee gets a raise'''
    raiseAmt = 1.00
    
    def __init__(self, name, contact, ID, pay):
        super().__init__(storeName = None, storeAddress = None)
        self.name = name
        self.contact = contact
        self.ID = ID
        self.pay = pay
        
        super.empList.append(self.name)
        
  
    #To get the email of the Enployee
    @property
    def email(self):
        return '{}@company.com'.format(self.name)
    
    #To Display the full-name of the Employee
    @property
    def fullname(self):
        return '{}'.format(self.name)
    
    #To changet the name of the Employee
    @fullname.setter
    def fullname(self,name):
        self.name = name
        
    #Give a store card to a customer
    def giveCard(self):
        return super.cardInfo()
    
    #apply a raise on pay of employee
    def applyRaise(self):
        self.pay *= raiseAmt
    
    #To fetch a list of all employees under the same manager as the employee    
    def disp_Current_Employees(self):
        return super.empList
    
    # To change the amount by which the Employee gets a raise
    @classmethod
    def set_raiseAmount(cls, amount):
        cls.raiseAmt = amount

    '''Allows Employee to quit the job'''        
    @classmethod
    def LeaveJob(cls,self):
        del self

'''
This Class Allows the user to register a customer into a store
It takes in the customer's ID, name and Contact
'''
class Customer(Store):
    
    purLis = {}
    '''
    This dictionary contains the Names and price of the 
    products that are in the customer's cart
    '''
    cost = 0
    
    def __init__(self, Customer_Name, ID, Contact, storeName, storeAddress, Budget):
        self.storeAddress = storeAddress
        self.storeName = storeName
        self.Customer_Name = Customer_Name
        self.ID = ID
        self.Contact = Contact
        self.Budget = Budget
    
        super().customer_log[self.Customer_Name] = ID

    '''
    Method to display the list of avaliable products in the store
    '''
    def showProds(self):
        return super.showProds()
    
    
    '''
    Method ot display all the products in the 
    cart of the Customer
    '''
    @classmethod
    def showPurchaseList(cls):
        
        print("Your Current Purchase List is:\n")
        print('Product Name\t\tProduct Price')
        
        for i in cls.purLis:
            try:
                print('\t{}\t|\t{}'.format(i,cls.purLus[i]))
            except:
                pass
    
    '''
    Method that Adds product to cart
    '''
    
    @classmethod
    def buyProds(cls, self):
        
        tempBudget = self.Budget
        
        while True:
            print("Your Remaining Budget:{}".format(tempBudget))
            print(Customer.showProds())
            print('\n\n',Customer.showPurchaseList())
            
            if str(input("Do you wish to continue [y/n]:")) == 'y':
                
                try:
                    prodName = str(input("Enter the name of the product:"))
                    cls.purLis[prodName] = super().prodLis[prodName]
                except:
                    print("E: Please enter a valid product Name")
                tempBudget -= super().prodLis[prodName]
                print("Remaining Budget: {}".format(tempBudget))
                if cls.cost >= Budget or tempBudget == self.Budget:
                    print("Out of money, please proceed to checkout")
                    break
                    
            else:
                break
        
        self.Budget = tempBudget
        cls.cost = self.Budget - tempBudget

    
    '''
    Method to remove a product from the cart
    '''
    @classmethod
    def remFromCart(cls,self):
        tempBudget = self.Budget
        
        while True:
            print(Customer.showProds())
            print('\n\n',Customer.showPurchaseList())
            
            if str(input("Do you wish to continue [y/n]:")) == 'y':
                
                try:
                    prodName = str(input("Enter the name of the product you wish to remove:"))
                    del cls.purLis[prodName]
                except:
                    print("E: Please enter a valid product Name")
                tempBudget += super().prodLis[prodName]
                    
            else:
                break
        self.Budget = tempBudget
        cost = self.Budget - tempBudget
        
    @classmethod
    def report(cls, self):
        with super().report as rep:
            print('Please start Writing your report\n\n')
            t = input("Please enter the date in format [dd/mm/yyyy]:")
            p = input("Enter Problem in a single line:")
            super().report.append(t+'\n')
            super().report.append(p+'\n\n')
            
    @classmethod
    def checkout(cls, self):
        print('Your Gross Cost is:{}'.format(sum(list(cls.purLis.values()))))
        if str(input("Do you wish to continue?[y/n]:")) == 'y':
            if cost > Budget:
                print("E: Your cost exceeds your budget")
            
            self.Budget -= cls.cost 
            print("Transaction Complete :D")
            print("Your Current Balance:{}".format(self.Budget))
            print("\nThank-You for your purchase. :)")
                    
            
        else:
            print("Exiting Checkout...")
            
                
        
    
    
    
    
    
    
    
