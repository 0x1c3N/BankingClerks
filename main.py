class Customer:
    
    def __init__(self,name,customer_type):
        self.name = name
        self.customer_type = customer_type
        ## we exptected different wait times for each unit of customers.
        if(customer_type=="commercial"):
           self.wait_time=10
        elif(customer_type=="casual"):
            self.wait_time=15
        elif(customer_type=="loan"):
            self.wait_time=20
        
    def display_info(self):
        """
        Display customer information.
        """
        print(f"Customer Name: {self.name}")
        print(f"Customer Type: {self.customer_type}")
        print(f"Customer Wait Time: {self.wait_time}")


commercial_customer=Customer(name="sinanbabawt",customer_type="commercial")

commercial_customer.display_info()
