from collections import defaultdict
import random
import datetime

class Customer:
    def __init__(self, name, customer_type):
        self.name = name
        self.arriving_time = 0
        self.customer_type = customer_type
        self.process_time=0   
    
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
        name = f"Customer{i+1}"
        customer_type = random.choice(customer_types)
        process_time = random.randint(5, 15)
        arriving_time = random.randint(0, 160)  # Generate random arriving time between 0 and 160 minutes
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

def min_clerks_for_customer_type(customers, clerk_count, wait_time=0):
    if not customers:  # Eğer müşteri kalmadıysa mevcut beklem süresine göre clerk sayısını döndür
        return clerk_count

    current_customer = customers[0]  # Kuyruktaki ilk müşteri
    remaining_customers = customers[1:]  # İlk müşteriyi kuyruktan çıkar

    # Eğer mevcut müşterinin beklemesi gereken süre 1 saati aşıyorsa yeni bir clerk oluştur ve recursive olarak devam et
    if wait_time > 60:
        return min_clerks_for_customer_type(list(customers), clerk_count + 1, 0)

    # Müşterinin bekleme süresini ve kalan müşterileri güncelle
    next_wait_time = wait_time + current_customer.process_time
    return min_clerks_for_customer_type(remaining_customers, clerk_count, next_wait_time)

random_customers = randomCustomer()

separated_customers = separate_customers_by_type(random_customers)

for customer_type, customer_list in separated_customers.items():
    print(f"{customer_type} Customers:")
    for customer in customer_list:
        print(f"Name: {customer.name}, Type: {customer.customer_type}")
    print("------------")

for customer_type, customer_list in separated_customers.items():
    min_clerk_count = min_clerks_for_customer_type(list(customer_list),0)
    print(f"Minimum clerk count for {customer_type}: {min_clerk_count}")