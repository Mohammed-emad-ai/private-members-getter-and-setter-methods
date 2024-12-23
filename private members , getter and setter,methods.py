class Geek:
	__name = None
	__roll = None
	__branch = None

	def __init__(self, name, roll, branch): 
		self.__name = name
		self.__roll = roll
		self.__branch = branch

	def __displayDetails(self):
		print("Name: ", self.__name)
		print("Roll: ", self.__roll)
		print("Branch: ", self.__branch)
	
	def accessPrivateFunction(self):
		self.__displayDetails() 

	def get_name(self):
		self.__name 
        
	def set_name(self , name):
		self.__name = name 

	def get_roll(self):
		self.__roll
        
	def set_roll(self , roll):
		self.__roll = roll 

	def get_branch(self):
		self.__branch
        
	def set_branch(self , branch):
		self.__branch = branch 
obj = Geek("Osama", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()
