from collections import defaultdict
import random
import datetime

maxWaitTimes = [60, 45, 60] #Default max waiting times for casual, commercial, loan

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
        print(f"Customer Name: {self.name}")
        formatted_arriving_time = datetime.datetime.strptime('09:00', '%H:%M') + datetime.timedelta(minutes=self.arriving_time)
        formatted_service_time = datetime.datetime.strptime('09:00', '%H:%M') + datetime.timedelta(minutes=self.serviceTime)
        formatted_arriving_time = formatted_arriving_time.strftime('%H:%M')  # Format time as hh:mm
        formatted_service_time = formatted_service_time.strftime('%H:%M')  # Format time as hh:mm
        print(f"Customer Arriving Time: {formatted_arriving_time}")
        print(f"Customer Service Time: {formatted_service_time}")
        print(f"Customer Wait Time: {self.waitTime}")
        print(f"Customer Process Time: {self.process_time}")
        print(f"Served Clercks: {self.clerkIndex}\n\n")

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
                        allCustomerFlag = False;
                if allCustomerFlag:
                    clerkFlag = True
                    break
                else:
                    timeFlag = True

    return (allClerks[clerksIndex])

def printCustomers(customers):
    for customer in customers:
        customer.display()

def main():

    # waitTimeChoice = input("Dou you want to set custom waiting times for Customer types? (Y,N) = ")

    # if (waitTimeChoice.upper() == "Y"):
    #     maxWaitTimeCasual = int(input("What do you want to set max wait time for Casual customer type: "))
    #     maxWaitTimeCommercial = int(input("What do you want to set max wait time for Commercial customer type: "))
    #     maxWaitTimeLoan = int(input("What do you want to set max wait time for Loan customer type: "))

    #     maxWaitTimes[0] = maxWaitTimeCasual
    #     maxWaitTimes[1] = maxWaitTimeCommercial
    #     maxWaitTimes[2] = maxWaitTimeLoan

    # else:
    #     if (waitTimeChoice.upper() != "N"):
    #         print("Wrong input!!, you should give only 'Y','y' or 'N','n'")
    #         exit(0)

    random_customers = randomCustomer()
    separated_customers = separate_customers_by_type(random_customers)

    for customer_type, customer_list in separated_customers.items():
        clercks =  min_clerk_algo(list(customer_list), customer_type)
        print( f"Customer Count:{len(customer_list)}", f"\nClerk Count:{len(clercks)}", f"\nType:{customer_type} \n\n")
        printCustomers(customer_list)

if __name__ == "__main__":

    main()