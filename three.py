#class and objects 

#banking class assignment

#trial code

from turtle import back


'''class UserModel():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def user_info(self):
        return f'Name: {self.name}, Age: {self.age}'

    def update_age(self, new_age):
        self.age = new_age
        return f'User {self.name} has been updated to age {self.age}'

    def update_name(self, new_name):
        self.name = new_name
        return f'User {self.name} has been updated'

user_obj = UserModel("Bob", 31)

result = user_obj.user_info()
print('result: ', result)

updated_age = user_obj.update_age(new_age=20)
print('updated_age: ', updated_age)

updated_name = user_obj.update_name(new_name="Alice")
print('updated_name: ', updated_name)

updated_class_values = user_obj.user_info()
print('updated_class_values: ', updated_class_values)'''



#banking assignment
class bank():
    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    
    def user_info(self):
        return f'name : {self.name},\n account number: {self.account_no},\n balance: {self.balance} '
    
    def withdraw(self, new_balance):
        self.balance  = new_balance
        return f'user {self.name} after withdraw 500, balance: {self.balance}'
    
    def deposit(self,new_deposit):
        self.balance = new_deposit
        return f'user {self.name} balance after new deposit balance: {self.balance} '
    
    def withdraw2(self, new_balance2):
        self.balance = new_balance2
        return f'user {self.name} balance after 2nd withdraw {self.balance}'
    


user_bank = bank("bob", 1234, 2000)

result = user_bank.user_info()
print('result: ', result)

withdraw = user_bank.withdraw(new_balance = 1500 )
print('new balance', withdraw)

deposit = user_bank.deposit(new_deposit=1700)
print('new balance', deposit )

withdraw2 = user_bank.withdraw2(new_balance2 = 700)
print( 'new balance', withdraw2 )


