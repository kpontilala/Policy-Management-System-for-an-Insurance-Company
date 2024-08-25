#!/usr/bin/env python
# coding: utf-8

# ## Policy Management System for an Insurance Company
# 
# #### Product class

# In[1]:


class Products:
    def __init__(self,name,Price,product_id):
        self.name = name
        self.Price = Price
        self.product_id = product_id
        self.active = True
        products = []
        
    def create_product(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price : ${self.Price:,}")
        print(f"Product ID: {self.product_id}")
    
    def update_product(self, new_name=None, new_Price=None):
        if new_name != self.name or new_Price != self.Price:
            self.name = new_name
            self.Price = new_Price
            
            print(f"Product with ID: {self.product_id} has been updated") 
            
        else:
            print('No update was carried out')
            
            
    def suspend_product(self):
        self.active = False
        print(f" product: {self.name} with ID: {self.product_id}, has been suspended")
        
    def reactivate_product(self):
        self.active = True
        print(f" product: {self.name} with ID: {self.product_id}, has been reactivated")


# In[ ]:




