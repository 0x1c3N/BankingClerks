import random
import datetime

class Customer:
    def __init__(self, name, customer_type):
        self.name = name
        self.wait_time = 0
        self.arriving_time = 0
        self.customer_type = customer_type
        if customer_type == "commercial":
            self.process_time = 10
        elif customer_type == "casual":
            self.process_time = 15
        elif customer_type == "loan":
            self.process_time = 20
    
    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer Type: {self.customer_type}")
        print(f"Customer Process Time: {self.process_time}")
        print(f"Customer Wait Time: {self.wait_time}")
        print(f"Customer Arriving zaza Time: {self.arriving_time}")
        # Calculate the arriving time in "hh:mm" format
        formatted_time = datetime.datetime.strptime('09:00', '%H:%M') + datetime.timedelta(minutes=self.arriving_time)
        formatted_time = formatted_time.strftime('%H:%M')  # Format time as hh:mm
        print(f"Customer Arriving Time: {formatted_time}")
        print("")

def randomCustomer():
    customer_types = ["commercial", "casual", "loan"]
    customers = []
    r = random.randrange(20, 60)
    for i in range(r):
        name = f"Customer{i+1}"
        customer_type = random.choice(customer_types)
        wait_time = random.randint(60, 180)
        arriving_time = random.randint(0, 180)  # Generate random arriving time between 0 and 180 minutes
        customer = Customer(name=name, customer_type=customer_type)
        customer.wait_time = wait_time
        customer.arriving_time = arriving_time
        customers.append(customer)
    return customers

random_customers = randomCustomer()
for customer in random_customers:
    print("-------------")
    customer.display_info()
