##############################################################################################################################
#  A class is like an object constructor, or a "blueprint" for creating objects. We instantiate a class to create an object.
# The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.
###############################################################################################################################


                        ####==> Creating a Class<==####
################################################################################# 
# To create a class we need the key word class followed by the name and colon.
#  Class name should be CamelCase.
##################################################################################
# syntax

# class ClassName:
#   code goes here

         ####==> Creating an Object <==####
# We can create an object by calling the class.

# p = Person()
# print(p)


                        ####==> Class Constructor <==####


############################################################################################################################################################
# In the examples above, we have created an object from the Person class. However, a class without a constructor is not really useful in real applications. 
# Let us use constructor function to make our class more useful. 
# Like the constructor function in Java or JavaScript, Python has also a built-in init() constructor function. 
# The init constructor function has self parameter which is a reference to the current instance of the class Examples:

# class Person:
#       def __init__ (self, name):
#         # self allows to attach parameter to the class
#           self.name =name

# p = Person('Asabeneh')
# print(p.name)
# print(p)
###############################################################################################################################################################


                        ####==> Inheritance <==####
##################################################################################################
# Using inheritance we can reuse parent class code. 
# Inheritance allows us to define a class that inherits all the methods and properties from parent class.
# The parent class or super or base class is the class which gives all the methods and properties.
# Child class is the class that inherits from another or parent class. 
# Let us create a student class by inheriting from person class.
#########################################################################################################


# class Student(Person):
#     pass


# s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
# s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
# print(s1.person_info())
# s1.add_skill('JavaScript')
# s1.add_skill('React')
# s1.add_skill('Python')
# print(s1.skills)

# print(s2.person_info())
# s2.add_skill('Organizing')
# s2.add_skill('Marketing')
# s2.add_skill('Digital Marketing')
# print(s2.skills)


# We did not call the init() constructor in the child class. If we didn't call it then we can still access all the properties from the parent.
# But if we do call the constructor we can access the parent properties by calling super.
# We can add a new method to the child or we can override the parent class methods by creating the same method name in the child class. 
# When we add the init() function, the child class will no longer inherit the parent's init() function.




                        ####==> Overriding parent method <==####


# class Student(Person):
#     def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
#         self.gender = gender
#         super().__init__(firstname, lastname,age, country, city)
#     def person_info(self):
#         gender = 'He' if self.gender =='male' else 'She'
#         return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

# s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
# s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
# print(s1.person_info())
# s1.add_skill('JavaScript')
# s1.add_skill('React')
# s1.add_skill('Python')
# print(s1.skills)

# print(s2.person_info())
# s2.add_skill('Organizing')
# s2.add_skill('Marketing')
# s2.add_skill('Digital Marketing')
# print(s2.skills)




                        ####==> 💻 Exercises: Day 21 Level 1<==####

class statistics:
    def __init__(self, lst):
        self.lst = lst
    def count(self):
        counter = 0
        for item in self.lst:
            counter += 1
        return counter    
    def sum(self):
        sumAll =0
        for item in self.lst:
            sumAll += item
        return sumAll    

    def min(self):
        min = self.lst[0]
        for item in self.lst:
            if item < min:
                min = item
        
        return min
    def max(self):
        max = self.lst[0]
        for item in self.lst:
            if item > max:
                max = item
        return max
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return round(self.sum() / self.count())
    
    def median(self):
        order = sorted(self.lst)
        center = self.count()//2
        return order[center]
    

    def mode(self):
        count_dic = {}
        for item in self.lst:
            if item in count_dic:

                count_dic[item] += 1
            else:
                count_dic[item] = 1    
        mode = [key for key, value in count_dic.items() if value == max(count_dic.values()) ]

        return {"mode":mode, "count": max(count_dic.values())}

    def std(self):
        sqtstd =0
        for item in self.lst:
            sqtstd += (item - self.mean())**2
        mean = sqtstd/ self.count()  
        std_dev = mean ** 0.5
        std_dev_rounded = round(std_dev,1)
        return std_dev_rounded  
    def var(self):
        Variance = self.std()**2
        return round(Variance,1)
    
    def freq_dist(self):
        freq_dic = {}
        order = sorted(self.lst)
        for item in order:
            if item in freq_dic:
                freq_dic[item] +=1
            else:
                freq_dic[item] = 1
        freq_dis = [(key , freq_dic[key] ) for key in freq_dic.keys()]
        return freq_dis

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() )# 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]




                        ####==> 💻 Exercises: Level 2 <==####

# Create a class called PersonAccount.
#  It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods.
#  Incomes is a set of incomes and its description. 
# The same goes for expenses.

class PersonAccount:
    def __init__(self,firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def   total_income(self):
        total = sum([value for value in self.incomes.values()])
        return total

    def  total_expense(self):
        total = sum([value for value in self.expenses.values()])
        return total
        
    def account_info(self):
        return {"firstName": self.firstname,"lastName": self.lastname}     

    def add_expense(self, new_expenses):
        for expense, amount in new_expenses.items():
            if expense in self.expenses:
                self.expenses[expense] += amount
            else:
                self.expenses[expense] = amount

    def add_income(self, new_income):
        for income, amount in new_income:
            if income in self.incomes:
                self.incomes[income] += amount
            else:
                self.incomes[income] = amount
                        

    def account_balance(self):
        return self.total_income() - self.total_expense()


incomes_data = {'Salary': 5000, 'Bonus': 1000, 'Investment': 2000}
expenses_data = {'Rent': 1200, 'Utilities': 200, 'Groceries': 300, 'Transportation': 150}

person1 = PersonAccount('Muhammad', 'Mubarak', incomes_data, expenses_data)

# Accessing data for person1
print("First Name:", person1.firstname)
print("Last Name:", person1.lastname)
print("Incomes:", person1.incomes)
print("Expenses:", person1.expenses)   
print("total income:", person1.total_income())
print("total expenses:", person1.total_expense()) 
print("Balance:", person1.account_balance())   