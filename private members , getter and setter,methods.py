class Geek:
	
	# private members
	__name = None
	__roll = None
	__branch = None

	# constructor
	def __init__(self, name, roll, branch): 
		self.__name = name
		self.__roll = roll
		self.__branch = branch

	# private member function 
	def __displayDetails(self):
		# accessing private data members
		print("Name: ", self.__name)
		print("Roll: ", self.__roll)
		print("Branch: ", self.__branch)
	
	# public member function
	def accessPrivateFunction(self):
		# accessing private member function
		self.__displayDetails() 

	# getter method for name
	def get_name(self):
		self.__name 
        
	# setter method name
	def set_name(self , name):
		self.__name = name 

	# getter method for roll
	def get_roll(self):
		self.__roll
        
	# setter method roll
	def set_roll(self , roll):
		self.__roll = roll 

	# getter method for branch
	def get_branch(self):
		self.__branch
        
	# setter method branch
	def set_branch(self , branch):
		self.__branch = branch 

             
# creating object 
obj = Geek("Osama", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()
