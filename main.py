from collections import defaultdict
import random
import datetime
import os

maxWaitTimes = [45, 30, 45] #Default max waiting times for casual, commercial, loan
shiftTime = ""
firstShift = "09:00"
secondShift = "12:00"
thirdShift = "15:00"
outputFileName = "output.txt"

"""
    Represents a customer in the simulation.

    Attributes:
    - name (str): The name of the customer.
    - clerkIndex (int): Index of the clerk serving the customer.
    - arriving_time (int): Arrival time of the customer.
    - customer_type (str): Type of the customer (casual, commercial, loan).
    - process_time (int): Processing time required for the customer.
    - maxWaitTime (int): Maximum wait time allowed for the customer.
    - waitTime (int): Time the customer waited before being served.
    - serviceTime (int): Time the customer was served.
    - isDone (bool): Flag indicating if the customer has been served.
"""
class Customer:
    def __init__(self, name, customer_type):
        self.clerkIndex = -1
        self.name = name
        self.arriving_time = 0
        self.customer_type = customer_type
        self.process_time = 0
        self.maxWaitTime =maxWaitTimes[0]
        if (customer_type == "commercial"):
            self.maxWaitTime = maxWaitTimes[1]
        elif (customer_type == "loan"):
            self.maxWaitTime = maxWaitTimes[2]
        self.waitTime = -1
        self.serviceTime = -1
        self.isDone = False

    def reset(self):
        self.isDone = False
        self.serviceTime = -1
        self.waitTime = -1

    def display(self):
        formatted_arriving_time = datetime.datetime.strptime(shiftTime, '%H:%M') + datetime.timedelta(minutes=self.arriving_time)
        formatted_service_time = datetime.datetime.strptime(shiftTime, '%H:%M') + datetime.timedelta(minutes=self.serviceTime)
        formatted_arriving_time = formatted_arriving_time.strftime('%H:%M')  # Format time as hh:mm
        formatted_service_time = formatted_service_time.strftime('%H:%M')  # Format time as hh:mm
        with open(outputFileName, "a") as outputFile:
            print(f"Customer Name: {self.name}", file=outputFile)
            print(f"Customer Arriving Time: {formatted_arriving_time}", file=outputFile)
            print(f"Customer Service Time: {formatted_service_time}", file=outputFile)
            print(f"Customer Wait Time: {self.waitTime}", file=outputFile)
            print(f"Customer Process Time: {self.process_time}", file=outputFile)
            print(f"Served Clercks: {self.clerkIndex}\n\n", file=outputFile)

"""
    Represents a clerk in the simulation.

    Attributes:
    - index (int): Index of the clerk.
    - currentCustomer (Customer): Customer currently being served.
    - isBusy (bool): Flag indicating if the clerk is busy.
    - availableTime (int): Time when the clerk will be available again.
"""
class Clerk:
    def __init__(self,index):
        self.index = index
        #self.process_time = processTime
        self.currentCustomer = Customer("null", "null")
        self.isBusy = False
        self.availableTime = -1
    def reset(self):
        self.isBusy = False
        self.currentCustomer = Customer("null", "null")
        self.availableTime = -1

def randomCustomer():
    customer_types = ["commercial", "casual", "loan"]
    customers = []
    for i in range(200):
        name = f"Customer{i + 1}"
        customer_type = random.choice(customer_types)
        customer = Customer(name=name, customer_type=random.choice(customer_types))
        customer.process_time = random.randint(5, 15)
        customer.arriving_time = random.randint(0, 100)  # Generate random arriving time between 0 and 100 minutes
        customers.append(customer)
        # Sorting custumers
    customers.sort(key=lambda x: x.arriving_time)
    return customers

"""
    Separates customers into different types.

    Args:
    - customers (list): List of Customer objects.

    Returns:
    - dict: Dictionary with customer types as keys and lists of customers as values.
"""

def separate_customers_by_type(customers):
    customer_types = defaultdict(list)

    for customer in customers:
        customer_types[customer.customer_type].append(customer)
    return customer_types

clerksCommercial = []
clerksCasual = []
clerksLoan = []
allClerks = [clerksCasual, clerksCommercial, clerksLoan]
time = 0
totalTime = 160

def reset_customers(customerList):
    for customer in customerList:
        customer.reset()

def reset_clerks(clerkList):
    for clerk in clerkList:
        clerk.reset()


"""
    Allocates customers to clerks using a minimum clerk algorithm.

    Args:
    - customers (list): List of Customer objects.
    - customer_type (str): Type of the customers to consider.

    Returns:
    - list: List of Clerk objects serving customers.
"""
def min_clerk_algo(customers, customer_type):
    clerksIndex = 0
    if customer_type == "commercial":
        clerksIndex = 1
    elif customer_type == "loan":
        clerksIndex = 2
    clerkFlag = False
    global totalTime
    while clerkFlag != True:
        allClerks[clerksIndex].append(Clerk(index=len(allClerks[clerksIndex])))
        reset_clerks(allClerks[clerksIndex])
        reset_customers(customers)
        waitingCustomer = []
        timeFlag=False
        for time in range(totalTime + 1):
            if timeFlag:
                break
            for customer in customers:
                if(customer.arriving_time <= time and customer.isDone == False and customer not in waitingCustomer):
                    waitingCustomer.append(customer)
            for _clerk in allClerks[clerksIndex]:
                if len(waitingCustomer)>0:
                    if _clerk.isBusy and _clerk.availableTime<=time:
                        _clerk.isBusy = False
                        _clerk.availableTime = -1
                        _clerk.currentCostumer.isDone = True
                    if not _clerk.isBusy:
                        _clerk.isBusy = True
                        _clerk.currentCostumer = waitingCustomer[0]
                        _clerk.availableTime = _clerk.currentCostumer.process_time + time
                        _clerk.currentCostumer.clerkIndex = _clerk.index
                        _clerk.currentCostumer.isDone = True
                        waitingCustomer.remove(_clerk.currentCostumer)
                        _clerk.currentCostumer.waitTime = time -  _clerk.currentCostumer.arriving_time
                        _clerk.currentCostumer.serviceTime = time
                        if _clerk.currentCostumer.waitTime > _clerk.currentCostumer.maxWaitTime:
                            timeFlag = True
            if time == totalTime:
                allCustomerFlag = True
                for customer in customers:
                    if customer.isDone == False:
                        allCustomerFlag = False
                if allCustomerFlag:
                    clerkFlag = True
                    break

    return (allClerks[clerksIndex])

"""
    Displays information for each customer in the list.

    Args:
    - customers (list): List of Customer objects.
"""

def printCustomers(customers):
    for customer in customers:
        customer.display()

"""
    Main function to run the simulation for a given shift.

    Args:
    - i (int): Shift index (0, 1, or 2).
"""
def main(i):

    global shiftTime

    if (i == 0):
        shiftTime= firstShift
    elif (i == 1):
        shiftTime= secondShift
    else:
        shiftTime= thirdShift

    random_customers = randomCustomer()
    separated_customers = separate_customers_by_type(random_customers)

    print(f"---------------------------- SHIFT {i+1} ----------------------------")
    for customer_type, customer_list in separated_customers.items():
        clercks =  min_clerk_algo(list(customer_list), customer_type)
        print( f"Customer Count:{len(customer_list)}", f"\nClerk Count:{len(clercks)}", f"\nType:{customer_type} \n\n")
        printCustomers(customer_list)

if __name__ == "__main__":

    if os.path.exists(outputFileName):
        os.remove(outputFileName)

    for i in range(0,3):
        main(i)

    print("[+] All details about Customers logged to output.txt file")