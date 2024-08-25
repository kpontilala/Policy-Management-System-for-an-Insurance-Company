#!/usr/bin/env python
# coding: utf-8

# ## Policy Management System for an Insurance Company
# 
# ##### Policy Holder's Class

# In[1]:


class PolicyHolders:
    existing_members = []
    
    def __init__(self,name,ID):
        
        self.AccountName = name
        self.PolicyHolder_ID = ID
        self.active = True
    
        
    def register_member(self):   #method for registring new members using ID
        for member in PolicyHolders.existing_members:
            if member.PolicyHolder_ID == self.PolicyHolder_ID:
                print("Policy Holder's ID already exist")
                return
            
        else:
            PolicyHolders.existing_members.append(self)
            print(f"Account Name:{self.AccountName}")
            print(f"Policy Holder's ID:{self.PolicyHolder_ID}")
            print(f"Active: {self.active}")
        
    def suspend_member(self):
        self.active = False
        print(f"Account Name: {self.AccountName} with ID: {self.PolicyHolder_ID}, has been suspended")
               
    def reactivate_member(self):
        self.active = True
        print(f"Account Name: {self.AccountName} with ID: {self.PolicyHolder_ID}, has been reactivated")
    
    def add_product(self,product):
        self.products.append(product)
        print(f"Product: {product.name} added to policy member with ID: {self.PolicyHolder_ID}")
    

              
        


# In[ ]:




