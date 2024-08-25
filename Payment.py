#!/usr/bin/env python
# coding: utf-8

# ## Policy Management System for an Insurance Company
# 
# #### Payment Class

# In[1]:


class Payments:
    def __init__(self,PolicyHolder_ID, product_id, amount):
        
        self.product_id = product_id
        self.amount = amount
        self.PolicyHolder_ID = PolicyHolder_ID
        self.payments=[]
       

    def process_payment(self,PolicyHolder_ID, product_id, amount):
        #creating a new payment instance
        payment = Payments(PolicyHolder_ID, product_id, amount)
        
        # Appending the payment to the payments list
        self.payments.append(payment)
        
        print(f"Payment for Policyholder ID: {payment.PolicyHolder_ID}, for Product ID: {payment.product_id}, is ${payment.amount:,})")

    def payment_reminder(self):
        print(f"Reminder sent to PolicyHolder: {self.PolicyHolder_ID}, for Product ID: {self.product_id}")

    def apply_penalty(self, penalty_amount):
        self.amount += penalty_amount
        print(f"Penalty of: ${penalty_amount:,}, new amount due: ${self.amount:,}")


# In[ ]:




