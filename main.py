from collections import defaultdict
import random
import datetime

#maxWaitTime = 30


class Customer:
    def __init__(self, name, customer_type):
        self.clerkIndex = -1
        self.name = name
        self.arriving_time = 0
        self.customer_type = customer_type
        self.process_time = 0
        self.maxWaitTime = 60
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

    def display_info(self):
        print(f"\n\nCustomer Name: {self.name}")
        print(f"Customer Type: {self.customer_type}")
        print(f"Customer Process Time: {self.process_time}")
        # Calculate the arriving time in "hh:mm" format
        formatted_time = datetime.datetime.strptime('09:00', '%H:%M') + datetime.timedelta(minutes=self.arriving_time)
        formatted_time = formatted_time.strftime('%H:%M')  # Format time as hh:mm
        print(f"Customer Arriving Time: {formatted_time}")
        print("")


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

    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer Type: {self.customer_type}")
        print(f"Customer Process Time: {self.process_time}")
        # Calculate the arriving time in "hh:mm" format
        formatted_time = datetime.datetime.strptime('09:00', '%H:%M') + datetime.timedelta(minutes=self.arriving_time)
        formatted_time = formatted_time.strftime('%H:%M')  # Format time as hh:mm
        print(f"Customer Arriving Time: {formatted_time}")
        print("")


def randomCustomer():
    customer_types = ["commercial", "casual", "loan"]
    customers = []
    r = random.randrange(20, 60)
    for i in range(200):
        name = f"Customer{i + 1}"
        customer_type = random.choice(customer_types)
        process_time = random.randint(5, 15)
        arriving_time = random.randint(1, 100)  # Generate random arriving time between 0 and 160 minutes
        customer = Customer(name=name, customer_type=customer_type)
        customer.process_time = process_time
        customer.arriving_time = arriving_time
        customers.append(customer)
        # Sorting custumers
    customers.sort(key=lambda x: x.arriving_time)
    return customers


def separate_customers_by_type(customers):
    customer_types = defaultdict(list)

    for customer in customers:
        customer_types[customer.customer_type].append(customer)
    return customer_types

#after copmparing those 2 methods we will decide to use one of them
"""def min_clerks_for_customer_type(customers, clerk_count, wait_time=0, memo={}):
    if not customers:
        return clerk_count

    key = (len(customers), clerk_count, wait_time)
    if key in memo:
        return memo[key]
    current_customer = customers[0]
    remaining_customers = customers[1:]
    if wait_time > 60:
        memo[key] = min_clerks_for_customer_type(list(customers), clerk_count + 1, 0, memo)
        return memo[key]
    next_wait_time = wait_time + current_customer.process_time
    memo[key] = min_clerks_for_customer_type(remaining_customers, clerk_count, next_wait_time, memo)
    return memo[key]
    
    def min_clerk_c(customers, customer_type):
    clerksIndex = 0
    if customer_type == "casual":
        clerksIndex = 1
    elif customer_type == "loan":
        clerksIndex = 2

    global time
    global totalTime
    simulatingTime = 0;
    while(simulatingTime<totalTime):
        reset_customers(customers)
        arrived_customer = []
        for customer in customers:
            if customer.arriving_time <= simulatingTime and customer.isDone == False:
                arrived_customer.append(customer)
        arrived_customer = (list(arrived_customer))
        if(len(arrived_customer) > 0):
            min_clerk(arrived_customer, clerksIndex, simulatingTime)
        simulatingTime += 1


def min_clerk(arrivedCustomer, clerkIndex, processTime):
    global time
    global totalTime
    _arrivedCustomer = arrivedCustomer
    lastCustomer = _arrivedCustomer[len(arrivedCustomer) - 1]
    while lastCustomer.waitTime < maxWaitTime:
        i = time
        clerk = Clerk(processTime)
        allClerks[clerkIndex].append(clerk)
        lastCustomer.waitTime = -1
        while i < totalTime:
            for _clerk in allClerks[clerkIndex]:
                if _clerk.availableTime <= i and _clerk.isBusy == True:
                    _clerk.isBusy = False
                if _clerk.isBusy == False:
                    if len(arrivedCustomer) == 0:
                        break
                    _customer = arrivedCustomer.pop(0)
                    _clerk.currentCostumer = _customer
                    _clerk.isBusy = True
                    _clerk.availableTime = i + processTime
                    _customer.waitTime = i - _customer.arriving_time
            i += 1
    """


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
                        _clerk.isBusy = False;
                        _clerk.availableTime = -1
                        _clerk.currentCostumer.isDone = True;
                    if not _clerk.isBusy:
                        _clerk.isBusy = True
                        _clerk.currentCostumer = waitingCustomer[0]
                        _clerk.availableTime = _clerk.currentCostumer.process_time + time
                        _clerk.currentCostumer.clerkIndex = _clerk.index
                        waitingCustomer.remove(_clerk.currentCostumer)
                        _clerk.currentCostumer.waitTime = time -  _clerk.currentCostumer.arriving_time
                        _clerk.currentCostumer.serviceTime = time
                        if _clerk.currentCostumer.waitTime > _clerk.currentCostumer.maxWaitTime:
                            timeFlag = True
            if time == totalTime:
                clerkFlag = True
                break

    reset_clerks(allClerks[clerksIndex])
    reset_customers(customers)
    waitingCustomer = []
    timeFlag = False
    for time in range(totalTime + 1):
        if timeFlag:
            break
        for customer in customers:
            if (customer.arriving_time <= time and customer.isDone == False and customer not in waitingCustomer):
                waitingCustomer.append(customer)
        for _clerk in allClerks[clerksIndex]:
            if len(waitingCustomer) > 0:
                if _clerk.isBusy and _clerk.availableTime <= time:
                    _clerk.isBusy = False;
                    _clerk.availableTime = -1
                    _clerk.currentCostumer.isDone = True;
                if not _clerk.isBusy:
                    _clerk.isBusy = True
                    _clerk.currentCostumer = waitingCustomer[0]
                    _clerk.availableTime = _clerk.currentCostumer.process_time + time
                    _clerk.currentCostumer.clerkIndex = _clerk.index
                    waitingCustomer.remove(_clerk.currentCostumer)
                    _clerk.currentCostumer.waitTime = time - _clerk.currentCostumer.arriving_time
                    _clerk.currentCostumer.serviceTime = time
                    if _clerk.currentCostumer.waitTime > _clerk.currentCostumer.maxWaitTime:
                        timeFlag = True


    return (allClerks[clerksIndex])

def printCustomers(customers):
    for customer in customers:
        customer.display();





random_customers = randomCustomer()

separated_customers = separate_customers_by_type(random_customers)

p = 0

for customer_type, customer_list in separated_customers.items():
    time = 45
    clercks =  min_clerk_algo(list(customer_list), customer_type)
    print( f"Customer Count:{len(customer_list)}", f"\nClerk Count:{len(clercks)}", f"\nType:{customer_type} \n\n")
    printCustomers(customer_list)
    p += 1
